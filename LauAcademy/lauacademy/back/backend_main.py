from queries import Queries
from video_gen import create_slideshow, gen_voice_img, tokenize
from text_to_image import get_ai
import json


def gen_vid(query):
    #print(query)
    slist = []
    aud = []
    img = []
    
    for x in query:
        #print(x['script'], '\n')
        title = (x['image_description'].replace(' ','+'))
        sentence = tokenize(x['script'])
        slist.append(sentence)
        a,b = gen_voice_img(title, sentence)
        aud.append(a)
        img.append(b)
        
        
        
    flatten_sentence = [item for sublist in slist for item in sublist]
    flatten_aud = [item for sublist in aud for item in sublist]
    flatten_img = [item for sublist in img for item in sublist] 
    
   
    create_slideshow('title', flatten_img, flatten_aud, flatten_sentence)
    
    
    return

QueryHandler = Queries("berkeleyhacks", 'atomic_habits.pdf')

slides = json.loads(QueryHandler["slides"]("How do beliefs shape habits"))
new = ((slides['sub_topics']))
title = ((new[0])['image_description']).replace(' ','+')

get_ai(title, QueryHandler['text_to_image']("test"))
#print(new)
#gen_vid(new)








