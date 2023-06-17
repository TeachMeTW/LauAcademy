import os
import dotenv

dotenv.load_dotenv()
from google.cloud import texttospeech

# Set the text input to be synthesized
target_text = "This is a test. This is a test. Double 07."

class TextToSpeech:
    def __init__(self):
        API_KEY = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        
    
    def synthesize_text(self, target_text):
        synthesis_input = texttospeech.SynthesisInput(text=target_text)
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=self.voice, audio_config=self.audio_config
        )
        
        with open("output.mp3", "wb") as out:
            # The response's audio_content is binary.
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')


# Test Code
# tts = TextToSpeech()
# tts.synthesize_text("Test Number 2. Google AI text voices")