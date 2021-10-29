r = int(input())

c = int(input())

graph = []

for i in range(r):
  l = list(map(int, input().split()))
  graph.append(l)
 


ans = 0


def island(graph, i, j, path):
  
  
  if(i<0 or j<0 or i>=r or j>=c or graph[i][j]==1 or graph[i][j]==-1):
    
    
  
  graph[i][j] = -1
  
  island(graph, i, j+1, path+"R")
  island(graph, i, j-1, path+"L")
  island(graph, i-1, j, path+"D")
  island(graph, i+1, j, path+"U")
  
  
  
  
for i in range(r):
  for j in range(c):
    if(graph[i][j]==0):
      path = ""
      a = island(graph,i,j, path)
      print(a)
      print(path)
      
    
  


print(ans)

