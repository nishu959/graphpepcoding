class forbfs:
  def __init__(self, x, y, time):
    self.x = x
    self.y = y
    self.time = time
    
      

m = int(input())
graph = []

for i in range(m):
  l = list(map(int, input().split()))
  graph.append(l)
  

visited = [[None for i in range(m+1)] for j in range(m+1)]

queue = []
dir = [[0,1],[1,0],[-1,0],[0,-1]]

def dfs(graph, i, j,visited , queue):
  visited[i][j] = 1
  
  queue.append(forbfs(i,j,0))
  for t in range(4):
    row_ = i + dir[t][0]
    col_ = j + dir[t][1]
    
    if(row_<0 or col_<0 or row_>=len(graph) or col_>=len(graph[0]) or visited[row_][col_]==1 or graph[row_][col_]==0):
      continue
    
    
    dfs(graph, row_, col_, visited, queue)
    
    

flag = False


for i in range(m):
  if(flag):
    break
  for j in range(m):
    if(graph[i][j]==1):
      dfs(graph, i, j, visited, queue)
      flag = True
      break
   
level = -1


t = False



while(len(queue)>0):
  if(t):
    break
  p = queue.pop(0)
  time = p.time
  
  for i in range(4):
    row_ = p.x + dir[i][0]
    col_ = p.y + dir[i][1]
    if(row_<0 or col_<0 or row_>=len(graph) or col_>=len(graph[0]) or visited[row_][col_]==1):
      continue
        
    if(graph[row_][col_]==1):
      t = True
      break
    
    queue.append(forbfs(row_,col_,p.time+1))
    
   
 
print(time)