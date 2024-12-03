import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text,'html.parser')

titleobj = soup.find_all(class_ = 'quote')
print(titleobj)