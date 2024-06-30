#binary array sort
ans = []
n = int(input())
l = list(map(int, input().split()))
ans.append(sorted(l))

for i in ans:
  print(i, end = " ")
print()
  
  
#max two
t = int(input())
ans = []
for _ in range(t):
  n = int(input())
  l=list(map(int,input().split()))
  ans.append(sorted(l)[:-2])

for i in ans:
  for j in i:
    print(j, end = " ")
  print()