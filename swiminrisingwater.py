
from heapq import heappop, heappush, heapify 

class edge:
  def __init__(self, src, nbr, wt):
    self.src = src
    self.nbr = nbr
    self.wt = wt


n = int(input())

graph = []
 

for i in range(n):
  a = list(map(int, input().split())) 
  graph.append(a)
  

 
 
class forbfs:
  def __init__(self, x, y, weigh):
    self.x = x
    self.y = y
    self.weigh = weigh
  
  def __lt__(self, com):
    return (self.weigh < com.weigh)
  
l = []
heapify(l)
heappush(l, forbfs(0,0,graph[0][0])) 
visited = [[False for i in range(n+1)] for j in range(n+1)] 
dir = [[0,1],[1,0],[0,-1],[-1,0]]
ans = -1

while(len(l)!=0):
  p = heappop(l)
  
  if(p.x==n-1 and p.y ==n-1):
    ans = p.weigh
    break
    
  
  if(visited[p.x][p.y]!=False):
    continue
  visited[p.x][p.y] = True
  
  for i in range(4):
    row_ = p.x + dir[i][0]
    col_ = p.y + dir[i][1]
    if(row_<0 or col_<0 or row_>=n or col_>=n):
      continue
    if(visited[row_][col_]==True):
      continue
    nwt = max(p.weigh, graph[row_][col_]) 
    heappush(l, forbfs(row_, col_, nwt))
    
    
print(ans) 
  
  


  
 
