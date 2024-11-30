import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.bbc.com'

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text,'html.parser')
#print(soup)
table = soup.find('table')
rows = table.find_all('tr')

masterlist = []

header = soup.find_all(class_='sc-8ea7699c-3 dhclWg')
for headers in header:
    masterlist.append(header.text)

df=pd.DataFrame(masterlist)
print(df)
   