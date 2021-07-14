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
 
 

def hampacy(graph, s, visited, psf, l):
  if(len(psf)==len(graph)):
    if s in l:
      print(psf+"*")
    else:
      print(psf+".")
  
  visited[s] = 1
  
  for i in graph[s]:
    if(visited[i.nbr]==0):
      npsf = psf + str(i.nbr)
      hampacy(graph, i.nbr , visited, npsf, l)
      
  visited[s] = 0
  
  
l = []
for i in graph[s]:
  l.append(i.nbr)
  
  
hampacy(graph, s, visited, str(s), l)


      