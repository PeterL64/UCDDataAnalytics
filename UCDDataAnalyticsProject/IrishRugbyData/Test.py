import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
Json_Data = r.json()
#print(Json_Data)

for k in Json_Data.keys():
    print(k + ': ', Json_Data[k])