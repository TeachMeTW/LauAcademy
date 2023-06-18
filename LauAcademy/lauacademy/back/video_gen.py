from moviepy.editor import *
import text_to_image
import eleven_tts
import nltk.data
from moviepy.video.tools.subtitles import SubtitlesClip
from queries import Queries
nltk.download('punkt')


" PRE PROCESS THE TEXT HERE USING REGEX"


"""
Input:
    Title: File Name
    Images: List of Image Dirs
    Audio: List of Audio Dirs
    Text: List of Strings
"""
def create_slideshow(title,images, audio, text):
    
    size = range(len(images))
    
    audmap = {}
    # textmap = {}
    imgmap = {}
    for x in size:
        aud_clip =  AudioFileClip(audio[x])
        duration = aud_clip.duration
        img = ImageClip(images[x]).set_duration(duration)
        
        
        audmap[f'amp_{x}'] = aud_clip
        
    
        imgmap[f'ic_{x}'] = img
        
        
        
        #clip = TextClip(text[x], fontsize=20, color='white', method='caption', stroke_color='black', stroke_width=1, align='south')

        #clip = clip.set_duration(duration)
        #textmap[f'txt_{x}'] = clip
        audmap[f'amp_{x}'] = AudioFileClip(audio[x])
        
    
    au = list(audmap.values())
    im = list(imgmap.values())
    #tx = list(textmap.values())
    
    combine_images = concatenate(im, method="compose")
    #combine_texts = concatenate(tx, method="compose")
    combine_aud = concatenate_audioclips(au)
    composite = CompositeVideoClip([combine_images])
    
    voiceover = composite.set_audio(combine_aud)
    voiceover.write_videofile(f'{title}.mp4', fps=24)
    
    return



def gen_voice_img_ai(title, sentence, QueryHandler):

    audio = []
    k = text_to_image.search(title)
    img = []
    #img = text_to_image.get(title,k,len(sentence))
    
    for x in range(len(sentence)):
        audio.append(f'{title}_{x}.mp3')
        eleven_tts.gen(f'{title}_{x}.mp3',sentence[x])
        #print("sentence: ", sentence)
        prompt = QueryHandler["sentence_to_prompt"](sentence[x])
        #print("prompt: ",prompt)
        img.append(QueryHandler["text_to_image"](prompt))
        
    return audio,img

def gen_voice_img(title, sentence):

    audio = []
    k = text_to_image.search(title)
    img = text_to_image.get(title,k,len(sentence))
    
    for x in range(len(sentence)):
        audio.append(f'{x}.mp3')
        eleven_tts.gen(f'{x}.mp3',sentence[x])
    return audio,img


def tokenize(f):
    
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentence = (tokenizer.tokenize(f))
    return sentence

'''
sent = tokenize('test.txt')
#print([x for x in sent])
aud,img = gen_voice_img('Blocks', sent)
create_slideshow('Blocks', img, aud, sent)
'''