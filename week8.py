#find the string in grid
def find(grid, word):
    rows = len(grid)
    cols = len(grid[0])

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def search(r, c, dr, dc):
        for char in word:
            #if not valid cell or not matching character
            if not is_valid(r, c) or grid[r][c] != char:
                return False
            r += dr
            c += dc
        return True

    directions = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1)]
    ans = []
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if search(r, c, dr, dc):
                    ans.append((r, c))
    return ans

ans = []
r,c = map(int,input().split())
l = []
for _ in range(r):
  row = input().strip().split()
  l.append(row)
res=find(l,input())
for j in res:
    print(j, end = " ")
print(end = ',\n')


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