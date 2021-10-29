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
  

def bfs(graph, i, j):
  queue = []
  queue.append(forbfs(i, j,0))
  
   
  dir = [[0,1],[1,0],[-1,0],[0,-1]]
  
  while(len(queue)):
    p = queue.pop(0)
    
    
    if(graph[p.x][p.y] == 0 or graph[p.x][p.y]==-5):
      continue
      
    graph[p.x][p.y] = -5
    
    for t in range(4):
      row_ = p.x + dir[t][0]
      col_ = p.y + dir[t][1]
      
      
      if(row_ <0 or col_ <0 or row_ >= len(graph) or col_>=len(graph[0])):
        continue
      
      if(graph[row_][col_]>=0):
        graph[i][j] = graph[row_][col_] + 1
        
        return
        
      queue.append(forbfs(row_, col_, graph[row_][col_] + 1))
      
      
    
  
for i in range(m):
  for j in range(n):
    if(graph[i][j]==1):
      graph[i][j] = -2
      
      
for i in range(m):
  for j in range(n):
    if(graph[i][j]==-2):
      
      bfs(graph,i,j)
      
      
        
         
for i in graph:
  print(*i)