r = int(input())

c = int(input())

graph = []

for i in range(r):
  l = list(map(int, input().split()))
  graph.append(l)
 

  
visited = [([0]*c) for i in range(r)] 


ans = 0


def island(graph, i, j, visited):
  
  if(i<0 or j<0 or i>=r or j>=c or visited[i][j]==1 or graph[i][j]==1):
    
    return 
  
  visited[i][j] = 1
  island(graph, i, j+1, visited)
  island(graph, i, j-1, visited)
  island(graph, i-1, j, visited)
  island(graph, i+1, j, visited)
  
  
for i in range(r):
  for j in range(c):
    if(visited[i][j]==0 and graph[i][j]==0):
      island(graph,i,j,visited)
      ans += 1
    
  


print(ans)

