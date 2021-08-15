import sys

v, e = map(int, input().split())
edges = [] 

for i in range(e):
  l = list(map(int, input().split())) 
  edges.append(l)
 
 
path = [sys.maxsize]*(v)

path[0]= 0
  
for i in range(0,v):
  for j in edges:
    
    
    if(path[j[0]]==sys.maxsize):
      continue
    
    if(path[j[0]] + j[2] < path[j[1]]):
      
      path[j[1]] =path[j[0]] + j[2] 
      

cycle = 0
  
for j in edges:
      
  if(path[j[0]]==sys.maxsize):
    continue
    
  if(path[j[0]] + j[2] < path[j[1]]):
    cycle = 1
    break
      
      
print(cycle)

    
      


