import requests
import json


data = requests.get('https://api.tvmaze.com/shows/180/alternatelists')

dicto = json.loads(data.text)


for dic in dicto:
    if dic == "url":
        print(dic)

