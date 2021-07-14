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
  
  


visited= [0]*v



    
def iscyclic(graph, s, visited):
  l = []
  
  l.append(s)
  
  
  while(len(l)!=0):
    p = l.pop(0)
    
    if(visited[p]==1):
      return True
      
      
    visited[p] = 1
    

    for i in graph[p]:
      
      if(visited[i.nbr]==0):
        
        l.append(i.nbr)
        
  return False
        

finalans = False



        
for i in range(v):
  if(visited[i]==0):
    
    ans = iscyclic(graph, i, visited)
    
    
    if(ans ==True):
      finalans = True
      break
      
      
      
print("true") if(finalans) else print("false")
      
      
      
      
    
 