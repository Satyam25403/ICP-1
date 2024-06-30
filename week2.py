#facing sun
def two(s):
  n,ans=s[0],1
  for i in s[1:]:
      if i>n:
          n=i
          ans+=1
  return ans

q=[]
n=int(input())
l=list(map(int,input().split(" ")))
q.append(two(l))
for i in q:
  print(i)
    
#row with max ones
def max_ones(matrix, num_rows, num_columns):
  counts = []
  for i in range(num_rows):
      count = 0
      for j in range(num_columns):
          if matrix[i][j] == 1:
              count += 1
      counts.append(count)
  
  return counts.index(max(counts))

# Example usage
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(m)]
print("Row with the maximum 1s:", max_ones(matrix, m, n))
