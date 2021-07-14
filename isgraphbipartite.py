class edge():
  def __init__(self,src, nbr, weigh):
    self.src = src
    self.nbr = nbr
    self.weigh = weigh
   
  
graph = {}
v = int(input())
e = int(input())


for i in range(v):
  graph[i]=[]
 

for i in range(e):
  a, b, c= map(int, input().split())
  graph[a].append(edge(a, b, c))
  graph[b].append(edge(b, a, c))
  
  
  
visited= [-1]*v


class forbfs():
  def __init__(self, data, level):
    self.data = data
    self.level = level
    

def iscyclic(graph, s, visited):
  l = []
  
  l.append(forbfs(s, -1))
  
  
  while(len(l)!=0):
    p = l.pop(0)
    
    if(visited[p.data]!=-1):
      
      if(p.level!=visited[p.data]):
       
        return False
    else:
      
      visited[p.data] = p.level
      
    
      for i in graph[p.data]:
      
        if(visited[i.nbr]==-1):
          
          lvl = p.level + 1
          l.append(forbfs(i.nbr,lvl))
        
  return True 


finalans = True

for i in range(v):
  
  if(visited[i]==-1):
    
    ans = iscyclic(graph, i, visited)
    
    
    if(ans ==False):
      finalans = False
      break   

      
print("true") if(finalans) else print("false")


