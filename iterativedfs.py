class edge():
  def __init__(self,src, nbr, weigh):
    self.src = src
    self.nbr = nbr
    self.weigh = weigh
   
  
graph = {}
v = int(input())
e = int(input())

visited= [0]*v

for i in range(v):
  graph[i]=[]
 

for i in range(e):
  a, b, c= map(int, input().split())
  graph[a].append(edge(a, b, c))
  graph[b].append(edge(b, a, c))
  
  
  
s = int(input())
visited= [0]*v


class forbfs():
  def __init__(self, data, psf):
    self.data = data
    self.psf = psf
    
    
def iterdfs(graph, s, visited):
  l = []
  
  l.append(forbfs(s, str(s)))
  
  
  while(len(l)!=0):
    p = l.pop()
    
    if(visited[p.data]==1):
      continue
      
    visited[p.data] = 1
    
    print(p.data,p.psf,sep="@")
    
    for i in graph[p.data]:
      
      if(visited[i.nbr]==0):
        nstr= p.psf + str(i.nbr)
        l.append(forbfs(i.nbr,nstr))
        
        

    
      
iterdfs(graph, s, visited)
      
      
    
 