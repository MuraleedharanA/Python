import requests
from bs4 import BeautifulSoup

url = 'https://realpython.com'

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text,'html.parser')
#print(soup)

titles = soup.find_all(class_='card-title')
for title in titles:
    print(title.text)