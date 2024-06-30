#numbers disappeared in the array
l=list(map(int,input().split(" ")))
maximum=max(l)

q=[i for i in range (1,maximum+1)]

k=[]
for i in q:
  if i not in l:
    k.append(i)
print(k)



#painters partition problem
def countPainters(boards, time):
    n = len(boards)  # size of array
    painters = 1
    boardsPainter = 0
    for i in range(n):
        #If the current board length can be painted in given time,
        #it allocates the board to the current painter.
        if boardsPainter + boards[i] <= time:
            # allocate board to current painter
            boardsPainter += boards[i]
        #Otherwise, it allocates the board to the next painter and increments the painter count.
        else:
            # allocate board to next painter
            painters += 1
            boardsPainter = boards[i]
    return painters

def findLargestMinDistance(boards, k):
    #initialize search range
    low = max(boards)
    high = sum(boards)
    #find the largest value of time such that the number of painters needed does not exceed k
    for time in range(low, high+1):
        if countPainters(boards, time) <= k:
            return time
    return low

ans=[]
k,n=map(int,input().split(" "))
l=list(map(int,input().split(" ")))
print(findLargestMinDistance(l,k))
