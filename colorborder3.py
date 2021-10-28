row = int(input())
col = int(input())
graph = []

for i in range(row):
  graph.append(list(map(int, input().split())))
  


R = int(input())
C = int(input())
 

color = int(input())


def disisland(graph, i, j, clr):
  s = -1
  
  if(i<0 or j<0 or i>=len(graph) or j>= len(graph[0]) or abs(graph[i][j])!=clr):
    return 
  
  if(abs(graph[i][j])==clr):
    s += 1
    
  if(graph[i][j]==-clr):
    return
    
  graph[i][j] = -clr
  
  disisland(graph, i-1, j, clr)  
  disisland(graph, i, j-1, clr)
  disisland(graph, i+1, j, clr)   
  disisland(graph, i, j+1, clr)
  
  
  if(s==4):
    
    graph[i][j] = clr
    
  
    


disisland(graph, R, C, graph[R][C])

for i in range(row):
  for j in range(col):
    if(graph[i][j]<0):
      graph[i][j] = color
      
      
for i in graph:
  print(i)
  
      
    
  



