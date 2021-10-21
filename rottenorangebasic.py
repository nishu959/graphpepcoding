import copy,sys

class forbfs:
  def __init__(self, x, y, lvl):
    self.x = x
    self.y = y
    self.lvl = lvl
    
  def __lt__(self, nxt):
    self.lvl < nxt.lvl
   

m, n = map(int, input().split())
graph = []

for i in range(m):
  l = list(map(int, input().split()))
  graph.append(l)
  
ans = copy.deepcopy(graph)    

def bfs(graph, i, j):
  queue = []
  queue.append(forbfs(i, j,1))
  
  visited = [[None for i in range(n)] for j in range(m)]
  dir = [[0,1],[1,0],[-1,0],[0,-1]]
  
  while(len(queue)):
    p = queue.pop(0)
    
    
    if(visited[p.x][p.y] == 1):
      continue
      
    visited[p.x][p.y] = 1
    
    for t in range(4):
      row_ = p.x + dir[t][0]
      col_ = p.y + dir[t][1]
      
      
      if(row_ <0 or col_ <0 or row_ >= len(graph) or col_>=len(graph[0])):
        continue
      if(graph[row_][col_]==0):
        continue
        
      if(graph[row_][col_]==2):
        
        ans[i][j] = p.lvl
        
        
        return
        
      queue.append(forbfs(row_, col_, p.lvl + 1))
      
for i in range(m):
  for j in range(n):
    if(graph[i][j]==1):
      
      ans[i][j] = -1
    if(graph[i][j]==2):
      ans[i][j] = 0
    
for i in range(m):
  for j in range(n):
    if(graph[i][j]==1):
      
      bfs(graph, i, j)
      
p = True      
res = -sys.maxsize 
  
for i in ans:
  if(p==False):
    break
    
  for j in i:
    if(j==-1):
      p = False
      
    res = max(res, j)
    
    
      
 
if(p):
  print(res)
  
else:
  print(-1)
  
      
      
    
    
    
    
   
    