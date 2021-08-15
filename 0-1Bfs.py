class edge:
  
  def __init__(self, src, nbr, wt):
    self.src = src
    self.nbr = nbr
    self.wt = wt
   

class forbfs:
 
  def __init__(self, data, wsf):
    self.data = data
    self.wsf = wsf
   

graph = {}

v, e = map(int, input().split())

for i in range(1,v+1):
  graph[i] = []
  
 
for i in range(e):
  
  a, b= map(int, input().split())
  graph[a].append(edge(a, b, 0))
  graph[b].append(edge(b, a, 1))
  
  
visited = [False]*(v+1)

def o1bfs(graph, visited, s, des):
  
  l = []
  l.append(forbfs(1, 0))
  
  while(len(l)!=0):
    
    p = l.pop(0)
    
    if(p.data==des):
      return p.wsf
    
    if(visited[p.data]!=False):
      continue
    
    visited[p.data] = True
    
    for i in graph[p.data]:
      
      if(visited[i.nbr]==False):
        
        nwt = p.wsf + i.wt
        
        if(i.wt==1):
          l.append(forbfs(i.nbr, nwt)) 
          
        else:
          l.insert(0,forbfs(i.nbr, nwt))
        
  return -1

  
print(o1bfs(graph, visited, 1, v))

  
  