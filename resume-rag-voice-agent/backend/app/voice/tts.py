import os
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

class TTSManager:
    """
    Handles converting text to speech using ElevenLabs.
    """
    def __init__(self):
        api_key = os.getenv("ELEVENLABS_API_KEY")
        self.client = ElevenLabs(api_key=api_key)

    def text_to_speech(self, text: str) -> bytes:
        """
        Converts text to speech and returns audio bytes.
        """
        audio_generator = self.client.generate(
            text=text,
            voice="Rachel",
            model="eleven_monolingual_v1"
        )

        # Combine the generator output into bytes
        audio_bytes = b"".join(audio_generator)
        return audio_bytes
