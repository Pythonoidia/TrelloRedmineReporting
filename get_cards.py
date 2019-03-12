import os
from trello import TrelloClient

api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']

client = TrelloClient(api_key=api_key, api_secret=api_secret)

all_boards = client.list_boards()
my_board = all_boards[2]
my_lists = my_board.list_lists()

print(my_lists)

def get_todo_item():
    to_do = []
    for card in my_lists:
        cards = card.list_cards()

print(get_todo_item())