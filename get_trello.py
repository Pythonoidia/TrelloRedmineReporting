import os
import requests

#variables
api_k = os.environ['api_key']
api_s = os.environ['api_secret']
idBoard = #BoardId
api_adress = 'https://api.trello.com/1/boards/{idBoard}?key={yourKey}&token={yourToken}'

# board info

"""
board_info = requests.get(api_adress.format(idBoard=idBoard, yourKey=api_k, yourToken=api_s))
board_info_json = board_info.json()

for key, val in board_info_json.items():
    if key not in ("prefs", "labelNames"):
        print(key, ":", val)
"""
# card info
card_info = requests.get('https://api.trello.com/1/boards/{idBoard}/cards?key={yourKey}&token={yourToken}'.format(idBoard=idBoard, yourKey=api_k, yourToken=api_s))
card_info_json = card_info.json()

for i in card_info_json:
    print(i["id"],":",i["name"])