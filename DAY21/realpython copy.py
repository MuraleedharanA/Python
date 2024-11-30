import requests
from bs4 import BeautifulSoup

url = 'https://unsplash.com/t/nature'

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text,'html.parser')
#print(soup)

images = soup.find_all('img',{'srcset':True})
print(len(images))
counter = 0
for image in images:
    imageurl = image
    imageurl = imageurl['src']
    print(imageurl)

    imgdata = requests.get(imageurl).content
    imgpath = "Image\sample"+str(counter)+".jpg"

    with open(imgpath,'wb') as img_hndler:
        img_hndler.write(imgdata)
    counter+=1
