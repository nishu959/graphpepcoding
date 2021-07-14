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
units = int(input())

visited= [0]*v


class forbfs():
  def __init__(self, data, time):
    self.data = data
    self.time = time
    

def infect(graph, s, visited, units):
  l = []
  
  l.append(forbfs(s, 1))
  
  count =0
  while(len(l)!=0):
    p = l.pop(0)
    
    if(visited[p.data]==1):
      continue
      
    visited[p.data] = 1
    
    if(p.time<=units):
      
      count+=1
      
    else:
      
      break
    
    for i in graph[p.data]:
      
      if(visited[i.nbr]==0):
        ntime= p.time + 1
        l.append(forbfs(i.nbr,ntime))
        
        
  print(count)      
        
   
    
      
infect(graph, s, visited, units)


      
      
    