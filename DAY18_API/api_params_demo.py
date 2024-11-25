import requests
import pandas as pd

url="https://api.open-meteo.com/v1/forecast"

params={
    'latitude' : '',
    'logtitude, '

}

response = requests.get(url,params)

if(response.status_code==200):
    print("Success")
    df=pd.DataFrame(response.json())
    print(df)
else:
    print(response.status_code)

