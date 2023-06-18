from elevenlabs import clone, generate, play, set_api_key, save
from elevenlabs.api import History

set_api_key("0f1801c616b70c75cc368c071b8fa507")


def gen(fname,text):
    audio = generate(text=text, voice='Antoni', model='eleven_multilingual_v1')
    save(audio, fname)
    return