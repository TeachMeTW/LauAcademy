from queries import Queries
from video_gen import create_slideshow, gen_voice_img, tokenize, gen_voice_img_ai
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


def gen_vid_ai(query, QueryHandler):
    #print(query)
    slist = []
    aud = []
    img = []
    
    for x in query:
        #print(x['script'], '\n')
        title = (x['image_description'].replace(' ','+'))
        sentence = tokenize(x['script'])
        slist.append(sentence)
        a,b = gen_voice_img_ai(title, sentence, QueryHandler)
        aud.append(a)
        img.append(b)
        
        
        
    flatten_sentence = [item for sublist in slist for item in sublist]
    flatten_aud = [item for sublist in aud for item in sublist]
    flatten_img = [item for sublist in img for item in sublist] 
    
   
    create_slideshow('title', flatten_img, flatten_aud, flatten_sentence)
    
    
    return


'''
Structure:
QueryHandler = Queries("berkeleyhacks", 'atomic_habits.pdf')

slides = json.loads(QueryHandler["slides"]("Name only one habit"))
new = ((slides['sub_topics']))

gen_vid(new)

'''









