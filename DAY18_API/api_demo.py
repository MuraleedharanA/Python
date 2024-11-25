import requests
import pandas as pd

url="https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if(response.status_code==200):
    print("Success")
    df=pd.DataFrame(response.json())
    print(df)
else:
    print(response.status_code)

