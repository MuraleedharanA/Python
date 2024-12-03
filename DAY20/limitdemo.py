import requests
import time

url= 'hhtps://api.open-meteo.com/vi/forecast'
params = {
    'latitude' : 12.9719,
    'longitude' : 77.5937,
    'current_weather' : 'true'
}

for item in range(100):
    response = requests.get(url,params)
    print(response)

    if(response.status_code == 200):
        print(response)
    elif(response.status_code==429):
        print("rate limit exeeded")
    else:
        print("other error")