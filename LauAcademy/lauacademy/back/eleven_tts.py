from elevenlabs import clone, generate, play, set_api_key, save
from elevenlabs.api import History

set_api_key("19e159289a5a4b42f0f8066359b0d7ea")


def gen(fname,text):
    audio = generate(text=text, voice='Bella', model='eleven_monolingual_v1')
    save(audio, fname)
    return