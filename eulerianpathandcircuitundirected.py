#undirected graph

#eulerian circuit = all degree even

#eulerian PATH = all degree even or (n-2 even degree and 2 odd degree)
#2 odd degree vertex will be source and destination 

v, e= map(int, input().split())

graph = {}

for i in range(v):
  graph[i] = []
  

for i in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
  
degree= [0]*(v)
for i in range(v):
  
  for j in graph[i]:
    degree[i] += 1
    
even = 0
odd = 0

for i in degree:
  
  if(i%2==0):
    even+=1
    
  else:
    odd+=1
    
    
if(even == v):
  print("Eulerian Circuit")
  
if((even == v-2 and odd ==2) or even == v):
  print("Eulerian Path")
  

  
  
  
