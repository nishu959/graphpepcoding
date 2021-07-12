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

"""
for i in range(v):
  for j in graph[i]:
    print(j.src,j.nbr,j.weigh)
   
"""


visited = [0]*v

def haspath(graph, s, d, visited):
  if(s==d):
    return True
  visited[s] = 1
  for i in graph[s]:
    if(visited[i.nbr] ==0):
      p = haspath(graph, i.nbr, d, visited)
      if(p==True):
        return True
        
  return False
      
    
print("true") if(haspath(graph,s, d, visited)) else print("false")
  