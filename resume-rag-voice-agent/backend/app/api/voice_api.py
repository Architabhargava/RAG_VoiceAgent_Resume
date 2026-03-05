import asyncio
import uuid
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from backend.app.voice.stt import STTManager
from backend.app.voice.tts import TTSManager
from backend.app.voice.session_manager import SessionManager
from backend.app.agents.resume_agent import ResumeAgent

router = APIRouter()
stt_manager = STTManager()
tts_manager = TTSManager()
session_manager = SessionManager()

@router.websocket("/voice")
async def voice_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time voice interaction.
    Accepts audio bytes, processes through RAG agent, and returns audio response.
    """
    await websocket.accept()
    session_id = str(uuid.uuid4())
    agent = ResumeAgent(session_id)

    print(f"New voice session started: {session_id}")

    try:
        while True:
            # 1. Receive audio data from client
            audio_data = await websocket.receive_bytes()

            # 2. Interruption handling: cancel previous processing if any
            session_manager.cancel_task(session_id)

            # 3. Define the response task
            async def process_voice_query(audio_bytes: bytes):
                try:
                    # a. STT
                    transcript = stt_manager.transcribe_audio(audio_bytes)
                    print(f"Transcript: {transcript}")

                    if not transcript.strip():
                        return

                    # b. Agent Query (RAG + Memory)
                    answer = await agent.answer_question(transcript)
                    print(f"Agent answer: {answer}")

                    # c. TTS
                    audio_response = tts_manager.text_to_speech(answer)

                    # d. Send audio back to client
                    await websocket.send_bytes(audio_response)
                except asyncio.CancelledError:
                    print(f"Task for session {session_id} was cancelled.")
                except Exception as e:
                    print(f"Error processing voice query: {e}")

            # 4. Create and register the task
            task = asyncio.create_task(process_voice_query(audio_data))
            session_manager.register_task(session_id, task)

    except WebSocketDisconnect:
        print(f"WebSocket disconnected for session: {session_id}")
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        session_manager.clear_session(session_id)
