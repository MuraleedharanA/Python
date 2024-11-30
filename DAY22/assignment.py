import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text,'html.parser')
#print(soup)
table = soup.find('table')
rows = table.find_all('tr')

masterlist = []

for row in rows:
    cells = row.find_all('td')
    data= [cell.text.strip() for cell in cells]
    masterlist.append(data)
    #print(data)
    #print(type(data))


df = pd.DataFrame(masterlist)
print(df)
df.to_csv('data.csv')