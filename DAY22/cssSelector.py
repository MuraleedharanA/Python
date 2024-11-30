import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

reponse = requests.get(url)

soup = BeautifulSoup(reponse.text,'html.parser')

titleobj = soup.find_all(class_ = 'quote')
textobj = titleobj.find(class_='text')
print(textobj.strip())

author_obj = titleobj.find(class_='author')
print(author_obj.strip())

quotes = soup.select(".quote .text")
authors = soup.select(".quotes .author")

for each_quote,each_author in zip(quotes,author):
    print(each_quote.text,"-",each_author.text)