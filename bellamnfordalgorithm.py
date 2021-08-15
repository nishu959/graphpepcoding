import sys

v, e = map(int, input().split())
edges = [] 

for i in range(e):
  l = list(map(int, input().split())) 
  edges.append(l)
 
 
path = [sys.maxsize]*(v+1)

path[1]= 0
  
for i in range(0,v):
  for j in edges:
    
    
    if(path[j[0]]==sys.maxsize):
      continue
    
    if(path[j[0]] + j[2] < path[j[1]]):
      
      path[j[1]] =path[j[0]] + j[2] 
      
    
    
path = path[2:]
  
print(*path)
  
  

  


