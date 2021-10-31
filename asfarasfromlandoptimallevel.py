class forbfs:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
    
      

m= int(input())
graph = []

for i in range(m):
  l = list(map(int, input().split()))
  graph.append(l)
  
  
queue = []
land = 0

for i in range(m):
  for j in range(m):
    if(graph[i][j]==1):
      queue.append(forbfs(i, j))
      
    if(graph[i][j]==0):
      land += 1
      
     
dir = [[0,1],[1,0],[-1,0],[0,-1]]

      
level = -1
while(len(queue)>0):
  level += 1
  size = len(queue)
  
  while(size>0):
    p = queue.pop(0)
    
    for i in range(4):
      row_ = p.x + dir[i][0]
      col_ = p.y + dir[i][1]
    
    
      if(row_<0 or col_<0 or row_>=len(graph) or col_>=len(graph[0]) or graph[row_][col_]!=0):
        continue
     
      queue.append(forbfs(row_, col_))
      graph[row_][col_] =  1
      
    size-= 1
 
if(land==0):
  print(-1)
else:
  print(level)
   
