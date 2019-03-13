import os
import requests
from datetime import datetime


#variables

api_k = os.environ['api_key']
api_s = os.environ['api_secret']
idBoard = '5c869a9077581523e219a895'
board_creation_date = datetime.fromtimestamp(int(idBoard[0:8],16))
api_adress = 'https://api.trello.com/1/boards/{idBoard}?key={yourKey}&token={yourToken}'


# board info

board_info = requests.get(api_adress.format(idBoard=idBoard, yourKey=api_k, yourToken=api_s))
board_info_json = board_info.json()

for key, val in board_info_json.items():
    if key not in ("prefs", "labelNames"):
        print(key, ":", val)

# cards info

card_info = requests.get('https://api.trello.com/1/boards/{idBoard}/cards?key={yourKey}&token={yourToken}'.format(idBoard=idBoard, yourKey=api_k, yourToken=api_s))
card_info_json = card_info.json()

# card id, date of creation, card name
for i in card_info_json:
    print(i["id"], ":", datetime.fromtimestamp(int(i["id"][0:8], 16)), ":", i["name"])

# card creator info - details action -- FUTURE
"""
card_details = requests.get('https://api.trello.com/1/cards/5c869d1e1f03c408d9fc636a/actions?action_memberCreator_fields&key={yourKey}&token={yourToken}'.format(idBoard=idBoard, yourKey=api_k, yourToken=api_s))
card_details_json = card_details.json()
print(card_details_json)
"""
# card creator info for specific card
card_details = requests.get('https://api.trello.com/1/boards/{idBoard}/actions?key={yourKey}&token={yourToken}&filter=createCard&fields=idMemberCreator&idModels=5c869d1e1f03c408d9fc636a'.format(idBoard=idBoard, yourKey=api_k, yourToken=api_s))
card_details_json = card_details.json()
#print(card_details_json)

slownik = {}
for i in card_details_json:
    slownik.update(i)

print(slownik)