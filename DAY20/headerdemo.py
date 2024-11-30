import requests

url = 'https://httpbin.org/headers'
headers = {"Custom-Header":"Rohith's"}
 
response = request.get(url, headers=headers)

print(response)
print(type(response))
print(response.headers)
print(response.json())
