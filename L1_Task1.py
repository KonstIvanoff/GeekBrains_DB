import requests, json
from pprint import pprint

mylogin = 'defunkt'
myurl = f'https://api.github.com/users/{mylogin}/repos'

r = requests.get(myurl)

# pprint(r.json())

flnm = 'userrepos.json'

if r.ok:
    with open(flnm, 'w') as strm:
        json.dump(r.json(), strm)
        print('Данные получены и сохранены!')
else:
    print('Не удалось получить данные!')


