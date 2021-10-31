class forbfs:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
    
      

m = int(input())
graph = []

for i in range(m):
  l = list(map(int, input().split()))
  graph.append(l)
  

visited = [[None for i in range(m+1)] for j in range(m+1)]

queue = []
dir = [[0,1],[1,0],[-1,0],[0,-1]]

def dfs(graph, i, j,visited , queue):
  if(i<0 or j<0 or i>=len(graph) or j>=len(graph[0]) or visited[i][j]==1 or graph[i][j]==0):
    return
  visited[i][j] = 1
  queue.append(forbfs(i,j))
  dfs(graph, i-1, j,visited , queue)
  dfs(graph, i+1, j,visited , queue)
  dfs(graph, i, j-1,visited , queue)
  dfs(graph, i, j+1,visited , queue)

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
  size = len(queue) 
  level += 1
  while(size>0):
    p = queue.pop(0)
    for i in range(4):
      row_ = p.x + dir[i][0]
      col_ = p.y + dir[i][1]
      if(row_<0 or col_<0 or row_>=len(graph) or col_>=len(graph[0]) or visited[row_][col_]!=None):
        continue
        
      if(graph[row_][col_]==1):
        t = True
        break
    
      queue.append(forbfs(row_,col_))
    size -= 1
   
 
print(level)