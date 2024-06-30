#celebrity problem
def id(matrix,r):
    index=0
    for i in matrix:
        if(all(ele==0 for ele in i)):
        #row has no 1
            return index
        index+=1
    return -1

m=int(input())
matrix = [list(map(int, input().split())) for i in range(m)]
print(id(matrix,m))


#nuts and bolts
def match_nuts(nuts,bolts):
    b=[]
    n=[]
    order=["!","#","$","%","&","*","@","^","~"]
    for i in order:
        if i in bolts:
            b.append(i)
    for i in order:
        if i in nuts:
            n.append(i)
            
    print(b,n,sep="\n")

n=int(input())
nuts=input().split(" ")
bolts=input().split(" ")
match_nuts(nuts,bolts)