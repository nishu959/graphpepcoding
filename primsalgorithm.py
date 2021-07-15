from heapq import heappop, heappush, heapify

class edge():
  def __init__(self,src, nbr, weigh):
    self.src = src
    self.nbr = nbr
    self.weigh = weigh
   
  
graph = {}
v = int(input())
e = int(input())

visited= [False]*v

for i in range(v):
  graph[i]=[]
 

for i in range(e):
  a, b, c= map(int, input().split())
  graph[a].append(edge(a, b, c))
  graph[b].append(edge(b, a, c))
  
  
  
s = 0



class forbfs():
  def __init__(self, data, ps,wt):
    self.data = data
    self.ps = ps
    self.wt = wt
    
  def __lt__(self, com):
    return (self.wt < com.wt)         
    
    
def spatw(graph, s, visited):
  l = []
  heapify(l)
  
  heappush(l,forbfs(s, -1, 0))
  
  
  while(len(l)!=0):
    
    p = heappop(l)
    
    
    if(visited[p.data]!=False):
      
      continue
    
    visited[p.data]=  True
    if(p.ps!=-1):
      print("[" +str(p.data) +"-"+str(p.ps) +"@"+str(p.wt)+"]")  
    
    
    for i in graph[p.data]:
     
      if(visited[i.nbr]==False):
        
        npsf = p.data
        nwt =  i.weigh
        
        heappush(l, forbfs(i.nbr, npsf, nwt))
    
    
  

   
      
spatw(graph, s, visited)

