
m, n = map(int, input().split())
graph = []

for i in range(m):
  l = list(map(int, input().split()))
  graph.append(l)
  


def disisland(graph, i, j):
  
  global s
  graph[i][j] = -3
  
  if(i-1>=0 and graph[i-1][j]==1):
    s += "u" 
    disisland(graph, i-1, j)
    
  
  if(j-1>=0 and graph[i][j-1]==1):
    s += "l"
    
    disisland(graph, i, j-1)
    
  
  if(i+1<len(graph) and graph[i+1][j]==1):
    s += "d"
    disisland(graph, i+1, j)
    
  
  
  if(j+1<len(graph[0]) and graph[i][j+1]==1):
    s += "r"
    disisland(graph, i, j+1)
  
  s += "z"
  
 

ans = []


for i in range(m):
  for j in range(n):
    
    
    if(graph[i][j]==1):
      s = "x"
       
      disisland(graph, i, j)
      
 
      ans.append(s)
      

print(len(set(ans)))

  