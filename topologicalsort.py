
class edge():
  def __init__(self, src, nbr):
    self.src = src
    self.nbr = nbr
   

v =int(input())
e =int(input())

graph = {}

for i in range(v):
  graph[i] = []
 

for i in range(e):
  a, b= map(int,input().split())
  graph[a].append(edge(a, b))
  

visited =[0]*v
 

def toposort(graph, s, visited, stack):
  visited[s] = 1
  
  for i in graph[s]:
    if(visited[i.nbr]==0):
      toposort(graph, i.nbr, visited,stack)
      
  stack.append(s)
      
stack = []     
for i in range(v):
  if(visited[i]==0):
    toposort(graph, i, visited,stack)
    
    
while stack:
  print(stack.pop())
    




