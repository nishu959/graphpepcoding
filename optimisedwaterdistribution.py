
from heapq import heappop, heappush, heapify 
class edge:
  def __init__(self, src, nbr, wt):
    self.src = src
    self.nbr = nbr
    self.wt = wt
  
v, e = map(int, input().split())
graph = {}

dig = list(map(int, input().split()))

for i in range(0,v+1):
  graph[i] = []

for i in range(e):
  a, b, c = map(int, input().split())
 
  graph[a].append(edge(a, b, c))
  graph[b].append(edge(b, a, c))
  

for i in range(1,v+1):
  graph[i].append(edge(i, 0,dig[i-1]))
  graph[0].append(edge(0, i,dig[i-1]))


  
class forbfs():
  def __init__(self, data, weigh):
    self.data = data
    self.weigh = weigh
    
  def __lt__(self, com):
    return (self.weigh < com.weigh)         
 
visited = [False]*(v+1)
    
ans = 0

def prims(graph, visited):
  global ans
  l = []
  heapify(l)
  
  heappush(l,forbfs(0, 0))
  
  
  while(len(l)!=0):
    
    p = heappop(l)
    
    
    if(visited[p.data]!=False):
      
      continue
    
    visited[p.data]=  True
    
    ans += p.weigh 
            
    for i in graph[p.data]:
     
      if(visited[i.nbr]==False):
        
        
        nwt =  i.wt
        
        
        heappush(l, forbfs(i.nbr, nwt))
    

prims(graph,visited)
print(ans)
   