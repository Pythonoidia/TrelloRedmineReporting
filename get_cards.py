import os
from trello import TrelloClient

# variables
api_k = os.environ['api_key']
api_s = os.environ['api_secret']
board_name_track = 'Board Trello redmine integration' # variable with name of Board to track

# API access
client = TrelloClient(api_key=api_k, api_secret=api_s)

# board access
all_boards = client.list_boards()
my_board = all_boards[2]  # need to find solution for that!
my_lists = my_board.list_lists()


print(all_boards)
print(my_board)
print(my_lists)


def get_cards():
    to_do = []
    for card in my_lists:
        cards = card.list_cards()
        if card.closed == False:
            for i in cards:
                to_do.append(i.name)
    return to_do

print(get_cards())


#nazwy card
#opisy card
#userzy card

