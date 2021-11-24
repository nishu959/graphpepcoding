v1, e = map(int, input().split())
graph = {}
for i in range(1,v1+1):
  graph[i] = []

for i in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
 

par = [None]*(v1+1)
disc = [None]*(v1+1) 
low = [None]*(v1+1)
art = [None]*(v1+1)

par[1] = -1



visited = [False]*(v1+1)
time = 0

def dfs(graph, visited, u):
  global time
  disc[u] = time
  low[u] = time
  time += 1
  count = 0
  
  
  visited[u] = True
  
  for v in graph[u]:
     
    if(par[u]==v):
      continue
    elif(visited[v]==True):
      low[u] = min(low[u], disc[v])
      
    else:
      par[v] = u
      count += 1
      dfs(graph, visited, v)
      
      
      low[u] = min(low[u], low[v])
      
      if(par[u] == -1):
        if(count >= 2):
          art[u] = True
      else:
        if(low[v]>=disc[u]):
          art[u] = True
        
 
dfs(graph, visited, 1)        
ans = 0
for i in art:
  if i==True:
    ans += 1
print(ans)
      
      
      
