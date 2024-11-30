import requests

url  = "https://jsonplaceholder.typicode.com/posts"
params = {
    "_page" : 1,
    "_limit" : 5
}

reponse = request.get(url,params=params)
print(reponse)
print(reponse.headers)
print(len(reponse.json()))
master_list = []
for item in range(10):
    params = {
    "_page" : item,
    "_limit" : 5
    }
    reponse = requests.get(url,params=params)
    posts = reponse.json()
    master_list.append(posts)

    if(not posts):
        print('no resp')

     