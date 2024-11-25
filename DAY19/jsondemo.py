import requests
import pandas as pd

url='https://api.coingecko.com/api/v3/simple/price'

params={'ids':'bitcoin,ethereum','vs_currencies':'inr'}

response = requests.get(url,params)
print(response.json())
print(response.json()['ethereum']['inr'])
