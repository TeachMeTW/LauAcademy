from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

set_api_key("7beb515e2721eef8f3ccf7ae1d325f8b")

audio = generate(text="Robin, the Rizzler of the East. His superpower; trauma from his past relationships. He is a man of Fortune and Free Will", voice='Bella', model='eleven_monolingual_v1')

play(audio)