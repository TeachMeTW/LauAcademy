import os
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
from google.cloud import texttospeech

# Initiates the Client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
target_text = "Konstantin Victoria, the Goat of the West."
synthesis_input = texttospeech.SynthesisInput(text=target_text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')