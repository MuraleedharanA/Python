import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text,'html.parser')

links = soup.find_all('a',href=True)
for link in links:
    if link['href'].startswith('https') and 'wiki' in link['href']:
        print(link['href'])