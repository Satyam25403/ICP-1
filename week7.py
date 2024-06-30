#remove all sub folders
k=input().split(" ")
k=sorted(k,key=len)
#If the first directory name (k[i]) is a substring of the second directory name (k[j]) followed by a '/',
# it appends the second directory name (k[j]) to the list l
l=[k[j] for i in range(len(k)-1) for j in range(i+1,len(k)) if k[i]+'/' in k[j]]
print(list(set(k)-set(l)))



#print numbers containing 123 in ascending order
ans = []
for i in input().split():
    if "1" in i and "2" in i and "3" in i:
        ans.append(int(i))  

if not ans:
    print(-1)
else:
    ans.sort()
    for k in ans:
        print(k, end=" ")
