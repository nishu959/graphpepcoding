row = int(input())
col = int(input())
graph = []

for i in range(row):
  graph.append(list(map(int, input().split())))
  


R = int(input())
C = int(input())
 

color = int(input())


def disisland(graph, i, j, clr):
  
  s = 0
  graph[i][j] = -clr
  
  if(i-1>=0 and abs(graph[i-1][j])==clr):
    s += 1
  
  if(i-1>=0 and graph[i-1][j]==clr):
    
    disisland(graph, i-1, j, clr)
    
  if(j-1>=0 and abs(graph[i][j-1])==clr):
    s += 1
    
  if(j-1>=0 and graph[i][j-1]==clr):
    
    disisland(graph, i, j-1, clr)
    
  if(i+1<len(graph) and abs(graph[i+1][j]) ==clr):
    s += 1
    
  if(i+1<len(graph) and graph[i+1][j]==clr):
    
    disisland(graph, i+1, j, clr)
    
  if(j+1<len(graph[0]) and abs(graph[i][j+1]) ==clr):
    s += 1
  
  if(j+1<len(graph[0]) and graph[i][j+1]==clr):
    
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
  
      
    
  



