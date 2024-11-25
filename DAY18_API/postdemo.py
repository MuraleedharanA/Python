import requests
import pandas as pd

url="https://jsonplaceholder.typicode.com/posts"

data={
    'title':'athira',
    'body': 'hello'
}

response = requests.post(url,json=data)

if(response.status_code==200):
    print("Success")
else:
    print(response.status_code)

