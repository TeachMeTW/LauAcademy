from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup


"""Generate URLS from Token"""
def search(tokenstring):
    htmldata = urlopen(f"https://unsplash.com/s/photos/{tokenstring}")
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    
    imgurls = list(map(lambda v: v['src'], images))
    return imgurls


"""Save 5 Images from URLS"""
def printfive(tokenstring, images):
    getfive = images[1:6]
    for x in range(len(getfive)):
        img_data = requests.get(getfive[x]).content
        with open(f'LauAcademy/media/{tokenstring}_{x}.jpg', 'wb') as handler:
            handler.write(img_data)
            