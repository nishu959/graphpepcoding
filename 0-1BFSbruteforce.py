from heapq import heappop, heappush, heapify 

class forbfs:
  def __init__(self, data, wt):
    self.data = data
    self.wt = wt
    
  def __lt__(self, other):
    return self.wt < other.wt
  
class edge:
  def __init__(self, src, des, weight):
    self.src = src
    self.des = des
    self.weight = weight


n,m = map(int, input().split())
graph = {}
for i in range(1,n+1):
  graph[i] = []
 

for i in range(m):
  u, v = map(int, input().split())
  graph[u].append(edge(u, v, 0))
  graph[v].append(edge(v, u, 1))


visited = [None]*(n+1)

def dijkstra(graph, s, visited, des):
  l = []
  heapify(l)
  l.append(forbfs(s, 0))
  while(len(l)!=0):
    p = heappop(l)
    
    if(p.data == des):
      return p.wt
      
    if(visited[p.data]==1):
      continue
    visited[p.data] = 1
    for i in graph[p.data]:
      
      if(visited[i.des]==None):
        
        nwt = p.wt + i.weight
        heappush(l, forbfs(i.des,nwt))
        
  return -1
        

print(dijkstra(graph, 1, visited, n)) 
