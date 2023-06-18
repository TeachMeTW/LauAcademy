from urllib.request import urlopen, Request
import requests
from queries import Queries
from bs4 import BeautifulSoup
from pexels_api import API
import json

pexapi = API("5ZYueTnMLnd4dfhS98WMJQLPHor1uiJ3myWJprHnpFLd16qQvU4nji0z")


"""Generate URLS from Token"""
def search(tokenstring):
    pexapi.search(tokenstring)
    imgurls = []
        # Get all photos in the page
    photos = pexapi.get_entries()
    for photo in photos:
        imgurls.append(photo.large)
        # For each photo print its properties
        # If there is no next page print the last page and end the loop
    return imgurls


"""Save Images from URLS"""
def get(tokenstring, images, end):
    
    get_img = images[1:end]
    #print(get_img)
    location = []
    for x in range(len(get_img)):
        img_data = requests.get(get_img[x]).content
        with open(f'LauAcademy/media/{tokenstring}_{x}.jpeg', 'wb') as handler:
            location.append(f'./LauAcademy/media/{tokenstring}_{x}.jpeg')
            handler.write(img_data)
            
    return location

