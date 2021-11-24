v1, e = map(int, input().split())
graph = {}
for i in range(0,v1):
  graph[i] = []

for i in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
 

par = [None]*(v1)
disc = [None]*(v1) 
low = [None]*(v1)
art = []

par[0] = -1



visited = [False]*(v1)
time = 0

def dfs(graph, visited, u):
  global time
  disc[u] = time
  low[u] = time
  time += 1
  
  
  
  visited[u] = True
  
  for v in graph[u]:
     
    if(par[u]==v):
      continue
    elif(visited[v]==True):
      low[u] = min(low[u], disc[v])
      
    else:
      par[v] = u
     
      dfs(graph, visited, v)
      
      
      low[u] = min(low[u], low[v])
    
      
        
      if(low[v]>disc[u]):
          art.append([u,v])
        
 
dfs(graph, visited, 0)        

print(art)          
      
      
      
