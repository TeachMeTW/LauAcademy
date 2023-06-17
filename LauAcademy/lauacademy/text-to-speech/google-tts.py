import os
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
from google.cloud import texttospeech

print(API_KEY)

client = texttospeech.TextToSpeechClient()
