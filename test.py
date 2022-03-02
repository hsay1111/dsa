
cards = [13, 11, 10, 7, 4, 3, 1, 0]

query = 7

def locate_card(cards, query):
    position = 0

    while True:

        if cards[position] == query:

            return position

        position += 1
        
    return -1


print(locate_card(cards, query))
      


