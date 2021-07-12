class edge():
  def __init__(self, src, nbr, weigh):
    self.src = src
    self.nbr = nbr
    self.weigh = weigh
   
  

graph = {}
v = 7

for i in range(v):
  graph[i] = []
  

graph[0].append(edge(0,1,10)) 
graph[0].append(edge(0,3,40)) 


graph[1].append(edge(1,0,10)) 
graph[1].append(edge(1,2,10)) 


graph[2].append(edge(2,1,10)) 
graph[2].append(edge(2,3,10)) 


graph[3].append(edge(3,0,40)) 
graph[3].append(edge(3,2,10)) 
graph[3].append(edge(3,4,2)) 


graph[4].append(edge(4,3,2)) 
graph[4].append(edge(4, 5,3)) 
graph[4].append(edge(4,6,8)) 


graph[5].append(edge(5,4,3)) 
graph[5].append(edge(5,6,3)) 


graph[6].append(edge(6,4,8)) 
graph[6].append(edge(6,5,3)) 


for i in range(v):
  for j in graph[i]:
    print(j.src,j.nbr,j.weigh)
  