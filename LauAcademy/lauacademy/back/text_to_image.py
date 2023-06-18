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
def get(tokenstring, images, end):
    get_img = images[1:end]
    location = []
    for x in range(len(get_img)):
        img_data = requests.get(get_img[x]).content
        with open(f'LauAcademy/media/{tokenstring}_{x}.jpg', 'wb') as handler:
            location.append(f'./LauAcademy/media/{tokenstring}_{x}.jpg')
            handler.write(img_data)
            
    return location