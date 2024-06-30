from collections import deque

def find_deck_arrangement(N):
    #initial arrangement of the deck such that
    #when cards are moved as described, they come out in increasing order.
    
    deck = deque()
    
    # Insert cards from N down to 1
    for card in range(N, 0, -1):
        deck.appendleft(card)  # Insert the current card at the front
        deck.rotate(card)      # Rotate the deck to the right by the current card's value
    
    return list(deck)


print(find_deck_arrangement(4))  # Output should be [1, 3, 2, 4]