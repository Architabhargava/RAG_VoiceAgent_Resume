import io
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class STTManager:
    """
    Handles converting audio bytes to text using OpenAI Whisper.
    """
    def __init__(self):
        self.client = OpenAI()

    def transcribe_audio(self, audio_bytes: bytes) -> str:
        """
        Sends audio bytes to Whisper and returns the transcript.
        """
        # OpenAI's audio API requires a file-like object with a name
        audio_file = io.BytesIO(audio_bytes)
        audio_file.name = "audio.wav"

        transcript = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

        return transcript.text
