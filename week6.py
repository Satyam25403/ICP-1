#number of instances of balloon
from collections import Counter
for i in input().split(" "):
    k=Counter(i)
    for i in k:
        if i=="l" or i=="o":
            k[i]=k[i]//2
    print(min(k["b"],k["l"],k["a"],k["o"],k["n"]))
    
    
#most common word
s=Counter(input().lower().split(" "))
k=input().split(" ")
s1=dict(sorted(s.items(),key=lambda item:item[1],reverse=True))
for i,j in s1.items():
    if i not in k:
        print(i)
        break