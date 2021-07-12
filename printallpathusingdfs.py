class edge():
  def __init__(self, src, nbr, weigh):
    self.src = src
    self.nbr = nbr
    self.weigh = weigh
   
  
v = int(input())
e = int(input())

graph = {}

for i in range(v):
  graph[i] = []
  
  
for i in range(e):
  a, b, c = map(int, input().split())
  graph[a].append(edge(a, b, c))
  graph[b].append(edge(b, a, c))  
  

s = int(input())
d = int(input())

visited = [0]*v

def printallpath(graph, s, d, visited, psf):
  if(s==d):
    
    print(psf)
    return
    
  visited[s] = 1
  
  for i in graph[s]:
    if(visited[i.nbr] ==0):
      npsf = psf + str(i.nbr)
      printallpath(graph, i.nbr, d, visited, npsf)
      
      
  visited[s] =0
  
  return
  
  

printallpath(graph, s, d, visited, "0")