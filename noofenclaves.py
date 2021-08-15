
m, n = map(int, input().split())
graph = []

for i in range(m):
  l = list(map(int, input().split()))
  graph.append(l)
  


def enclave(graph, i, j):
  if(i<0 or j<0 or i>=m or j>=n or graph[i][j]==0):
    return    
 
  graph[i][j] = 0
  
  enclave(graph, i-1, j)
  
  enclave(graph, i+1, j )
  
  enclave(graph, i, j-1)
  
  enclave(graph, i, j+1)



for i in range(m):
  for j in range(n):
    
    if((i==0 or i==m-1 or j==0 or j==n-1) and (graph[i][j] == 1)):
      enclave(graph, i, j)
      


count = 0
for i in graph:
  for j in i:
    
    if(j==1):
      count += 1

print(count)

  