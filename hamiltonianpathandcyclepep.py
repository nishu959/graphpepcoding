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
 
 

def hampacy(graph, s, visited, psf, orsrc):
  if(len(psf)==len(graph)):
   
    pathorcycle = False
    
    for i in graph[s]:
      if(i.nbr==orsrc):
        pathorcycle = True
        break
    
    if(pathorcycle):
      print(psf+ "*")
      
    else:
      print(psf+ ".")
     
  visited[s] = 1
  
  for i in graph[s]:
    if(visited[i.nbr]==0):
      npsf = psf + str(i.nbr)
      hampacy(graph, i.nbr , visited, npsf, orsrc)
      
  visited[s] = 0
  
  
  

hampacy(graph, s, visited, str(s), s)


      