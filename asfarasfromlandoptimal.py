class forbfs:
  def __init__(self, x, y, time):
    self.x = x
    self.y = y
    self.time = time
    
    
  

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
      queue.append(forbfs(i, j,0))
      
    if(graph[i][j]==0):
      land += 1
      graph[i][j] = -1
     
dir = [[0,1],[1,0],[-1,0],[0,-1]]

      

while(len(queue)!=0):
  p = queue.pop(0)
  
  time = p.time
  for i in range(4):
    row_ = p.x + dir[i][0]
    col_ = p.y + dir[i][1]
    
    
    if(row_<0 or col_<0 or row_>=len(graph) or col_>=len(graph[0]) or graph[row_][col_]!=-1):
      continue
    
    graph[row_][col_]= p.time + 1
       
    queue.append(forbfs(row_, col_,p.time+1 ))
 
 
if(land==0):
  print(-1)
else:
  print(time)
   
