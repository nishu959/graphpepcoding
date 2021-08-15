from heapq import heappop, heappush, heapify 

class edge:
  def __init__(self, src, nbr, wt):
    self.src = src
    self.nbr = nbr
    self.wt = wt
    
    
class forpq:
  def __init__(self, data, pqwt):
    self.data = data
    self.pqwt = pqwt
    
  def __lt__(self, nxt):
    return (self.pqwt < nxt.pqwt)
  
  
def fun(graph, visited, s):
  ans = 0
  l = []
  heapify(l)
  heappush(l, forpq(0,0))
  
  
  while(len(l)>0):
    
    p = heappop(l)
    if(visited[p.data] == True):
      continue
      
    visited[p.data] = True
    ans += p.pqwt
    
    for i in graph[p.data]:
      if(visited[i.nbr] ==False):
        nwt = i.wt
        heappush(l, forpq(i.nbr,nwt))
        
    
  return ans
      
   

v = int(input())
e = int(input())

graph = {}

for i in range(v):
  graph[i] = []

for i in range(e):
  a, b, c = map(int, input().split())
  
  graph[a].append(edge(a,b,c))
  graph[b].append(edge(b,a,c))
  
  
visited = [False]*v

print(fun(graph, visited, 0)) 
  


