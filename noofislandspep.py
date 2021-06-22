
m =int(input())
n =int(input())
graph = []

for i in range(m):
  graph.append(list(map(int, input().split())))
  
count = 0 

visited = [([0]*n) for i in range(m)]

def noofisland(graph, i, j, visited):
  if(i<0 or j<0  or i>=m or j>=n or visited[i][j]==1 or graph[i][j]==1): 
    return
  visited[i][j] =1
  noofisland(graph, i-1,j,visited)
  noofisland(graph, i,j+1,visited)
  noofisland(graph, i,j-1,visited)
  noofisland(graph, i+1,j,visited)


for i in range(m):
  for j in range(n):
    if(graph[i][j]==0 and visited[i][j]==0):
      noofisland(graph, i, j, visited)
      count+=1
      

print(count)

  
  
