from moviepy.editor import *
import text_to_image
import eleven_tts

"""
    ic_1 = ImageClip('./LauAcademy/media/test/grass.jpg').set_duration(7)
    ic_2 = ImageClip('./LauAcademy/media/test/shower.jpg').set_duration(7)
    ic_3 = ImageClip('./LauAcademy/media/test/woman.jpg').set_duration(7)
    aud = AudioFileClip("./LauAcademy/media/test/imagine.mp3")

    txt_clip = TextClip("Things League Players are scared of",fontsize=70,color='black')

    # Say that you want it to appear 10s at the center of the screen
    txt_clip = txt_clip.set_pos('center').set_duration(5)


    video = concatenate([ic_1, ic_2, ic_3], method="compose")
    test1 = CompositeVideoClip([video, txt_clip])
    test2 = test1.set_audio(aud)

    test2.write_videofile('test.mp4', fps=24)
"""

" PRE PROCESS THE TEXT HERE USING REGEX"



def create_slideshow(title,images, audio, text):
    
    size = range(len(images))
    
    audmap = {}
    textmap = {}
    imgmap = {}
    for x in size:
        aud_clip =  AudioFileClip(audio[x])
        duration = aud_clip.duration
        audmap[f'amp_{x}'] = aud_clip
        
        imgmap[f'ic_{x}'] = ImageClip(images[x]).set_duration(duration)
        clip = TextClip(text[x], fontsize=20, color='white')
        clip = clip.set_pos('center').set_duration(duration)
        textmap[f'txt_{x}'] = clip
        audmap[f'amp_{x}'] = AudioFileClip(audio[x])
        
    
    au = list(audmap.values())
    im = list(imgmap.values())
    tx = list(textmap.values())
    
    combine_images = concatenate(im, method="compose")
    combine_texts = concatenate(tx, method="compose")
    combine_aud = concatenate_audioclips(au)
    composite = CompositeVideoClip([combine_images, combine_texts])
    
    voiceover = composite.set_audio(combine_aud)
    voiceover.write_videofile(f'{title}.mp4', fps=24)
    
    return


k = text_to_image.search('Map')
im = text_to_image.get('Map',k,3)
audio = []
title = 'Pooper'

sentence = ["In this first slide, we will learn how to work with Phoenix Channels by establishing a connection from the client to the channel running on the server.", "To accomplish this, we need to create a new socket object and pass it a path to the socket."]

for x in range(len(sentence)):
    audio.append(f'{x}.mp3')
    eleven_tts.gen(f'{x}.mp3',sentence[x])

create_slideshow(title=title, images=im, audio=audio, text=sentence)