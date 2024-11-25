import requests
from bs4 import BeautifulSoup

url = 'https://unsplash.com/s/phptos/nature'

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text,'html.parser')
#print(soup)

images = soup.find_all('img',{'srcset':True})

imageurl = images[-1]
imageurl = imageurl['src']

imgdata = requests.get(imageurl).content
imgpath = "sample.jpg"

with open(imgpath,'wb') as img_hndler:
    img_hndler.write(imgdata)
