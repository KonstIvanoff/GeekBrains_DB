import requests, json
from pprint import pprint

myurl = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

# 55.914070, 37.707799
pos = {"lon":"37.707799","lat":"55.914070"}
headers = {'x-rapidapi-key': "a064574773msh9d908f870146dcfp1bdaeejsnc6a58de2920c"}

res = requests.get(myurl, headers=headers, params=pos)

# pprint(res.json())

if res.ok:
    with open('weather.json','w') as st:
        json.dump(res.json(),st)
        print('Прогоноз погоды получен!')