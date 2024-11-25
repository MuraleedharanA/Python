import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text,'html.parser')
#print(soup)

h1_tag = soup.find('h1')
if h1_tag:
    print(h1_tag)

links = soup.find_all('a')
for link in links:
    href = link.get('href')
    print(link)

paras = soup.find_all('p')
for para in paras:
    print(para.text)

