import requests
import pandas as pd

url = 'https://programming-quotesapi.vercel.app/api/random'
url2 = 'https://api.microlink.io'

params={'url' : 'https://www.msn.com/en-in/autos/news/cars-owned-by-ratan-tata-from-tata-nexon-to-ferrari-california-check-out-the-list/ar-AA1t0gx0?ocid=msedgntp&pc=U531&cvid=c7200c36db5245b79c1f8e2443204186&ei=31'}

response = requests.get(url2,params)

if(response.status_code==200):
    df=pd.DataFrame(response.json())
    print(df['data']['description'])
else:
    print(response.status_code,response.reason)


