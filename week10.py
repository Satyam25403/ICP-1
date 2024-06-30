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


#queue using stacks
n = int(input())
l = list(map(int, input().split()))
queue = []
k = 0
for i in range(n):
  if l[k] == 1:
    queue.append(l[k+1])
    k += 2
  elif l[k] == 2:
    if queue:
      print(queue.pop(0),end = " ")
    else:
      print(-1, end = " ")
    k += 1
print()