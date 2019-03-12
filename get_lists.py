from trello import TrelloClient

client = TrelloClient(api_key='241061d740372ffdb4ad7902ae908261', api_secret='8a58e6ab452564a9539c13fd546e59b728c073de4d0b7a23dc2793326c96f5f2')

all_boards = client.list_boards()
my_board = all_boards[2]
my_lists = my_board.list_lists()

print(my_lists)