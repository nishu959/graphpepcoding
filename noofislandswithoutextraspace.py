r = int(input())

c = int(input())

graph = []

for i in range(r):
  l = list(map(int, input().split()))
  graph.append(l)
 


ans = 0


def island(graph, i, j):
  
  if(i<0 or j<0 or i>=r or j>=c or graph[i][j]==1 or graph[i][j]==-1):
    
    return 
  
  graph[i][j] = -1
  island(graph, i, j+1)
  island(graph, i, j-1)
  island(graph, i-1, j)
  island(graph, i+1, j)
  
  
for i in range(r):
  for j in range(c):
    if(graph[i][j]==0):
      island(graph,i,j)
      ans += 1
    
  


print(ans)

