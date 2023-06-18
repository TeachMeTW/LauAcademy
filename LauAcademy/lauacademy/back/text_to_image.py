from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup


"""Generate URLS from Token"""
def search(tokenstring):
    site = (f"https://www.pexels.com/search/{tokenstring}/")
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,'html.parser')
    images = soup.find_all('img')
    
    imgurls = list(map(lambda v: v['src'], images))
    return imgurls


"""Save Images from URLS"""
def get(tokenstring, images, end):
    get_img = images[1:end]
    location = []
    for x in range(len(get_img)):
        img_data = requests.get(get_img[x]).content
        with open(f'LauAcademy/media/{tokenstring}_{x}.jpg', 'wb') as handler:
            location.append(f'./LauAcademy/media/{tokenstring}_{x}.jpg')
            handler.write(img_data)
            
    return location