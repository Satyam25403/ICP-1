#leaders in an array
def leader(l):
    a=[]
    for i in range(len(l)):
        if i==len(l)-1:
            #last element is always a leader
            a.append(l[i])
        elif greater(l[i],l[i+1:]):
            #element is greater than all elements to its right
            a.append(l[i])
    return a

def greater(n,m):
    for i in m:
        if i>n:
            return False
    return True

n=int(input())
l=list(map(int,input().split(" ")))
ans=leader(l)
for i in ans:
    print(i,end=" ")
    

#position of given element
def pos(l,n):
    if n not in l:
        l.append(n)
        l.sort()
        return l.index(n)
    else:
        return l.index(n)
print(pos([1,3,5,6],0))