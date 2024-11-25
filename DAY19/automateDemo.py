import requests
import datetime
import json

url = 'https://api.exchangrrate.host/latest'
params={'base':'USD'}

response = requests.get(url,params)
print(response)

if(response.status==200):
    rates =  response.json()['rates']
    filename = "exchange_rates_{val}.json.format"