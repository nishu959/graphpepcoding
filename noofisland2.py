class edge:
  def __init__(self, typeof, src, nbr):
    self.typeof = typeof
    self.src = src
    self.nbr = nbr
  
  
m, n, e = map(int, input().split())
l = []
  
cell = m * n 
par = [-1]*(cell)
rank = [1]*(cell)

graph = []

for i in range(m):
  q= [0]*n
  graph.append(q)
    
    
for i in range(e):
  a, b = map(int, input().split())
  l.append([a, b])
  

 
def find(x):
  if(par[x]==x):
    return x
  temp = find(par[x])
  par[x] = temp
  return temp
  
def union(x, y):
  lx = find(x)
  ly = find(y)
  if(lx!=ly):
    if(rank[lx]>rank[ly]):
      par[ly] = lx
    elif(rank[lx]<rank[ly]):
      par[lx] = ly
    else:
      par[lx] = y
      rank[ly]+=1
    
    return True  
  return False
 
 
dir = [[0,1],[1,0],[-1,0],[0,-1]]
ans = 0
result = []


for i in l:
  
  cell1 = i[0] * n + i[1]
  graph[i[0]][i[1]] = 1
  
  
  par[cell1] = cell1
  ans += 1
  for p in range(4):
    row_ = i[0] + dir[p][0]
    col_ = i[1] + dir[p][1]
    if(row_<0 or col_<0 or row_>=m or col_>=n):
      continue
    if(graph[row_][col_]==1):
      cell2 = row_ * n + col_
      boolmerge = union(cell1, cell2)
      if(boolmerge):
        ans -= 1
      
  
  result.append(ans)
      
      
print(result)    
      
      

