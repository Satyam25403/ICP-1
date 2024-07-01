#find the string in grid
m = int(input())
g = [list(input()) for _ in range(m)]
x = input()
y = 'a' * len(x)
for i in range(len(g)):
    row_string = ''.join(g[i])
    start = 0
    while start < len(row_string):
        d = row_string.find(x, start)
        if d == -1:
            break
        print(i, d)
        for j in range(len(x)):
            g[i][d + j] = y[j]
        start = d + len(x)



#missing number in matrix
def val(matrix,n):
    r_sum,c_sum,res=[],[],[]
    d1=0
    d2=0
    for i in range(n):
        c=0
        r=0
        for j in range(n):
            c+=matrix[i][j]
            r+=matrix[j][i]
            if(i==j):
                d1+=matrix[i][j]
            if(j==n-i-1):
                d2+=matrix[i][j]
        c_sum.append(c)
        r_sum.append(c)
    
    res=c_sum+r_sum
    res.append(d1)
    res.append(d2)
    
    if(res.count(min(res))==3):
        return max(res)-min(res)
    else:
        return -1
    
m=int(input())
matrix = [list(map(int, input().split())) for i in range(m)]
print(val(matrix,m))