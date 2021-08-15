
def sdfs(graph, visited, s, stack):
  
  visited[s] = True
  
  for i in graph[s]:
    if(visited[i]==False):
      sdfs(graph, visited, i, stack)   
      
  stack.append(s)
  
  
def dfs(graph, visited, s):
  
  visited[s] = True
  
  for i in graph[s]:
    if(visited[i]==False):
      dfs(graph, visited, i)   
        


v, e = map(int, input().split())


graph = {}

for i in range(1,v+1):
  graph[i] = []
  
  
for i in range(e):
  
  a, b = map(int, input().split())
  graph[a].append(b)
 


stack = [] 
visited =[False]*(v+1)


for i in range(1,v+1):
  if(visited[i]==False):
    sdfs(graph, visited, i, stack)


visited =[False]*(v+1) 



stacktop  = stack.pop()



dfs(graph, visited, stacktop)




ans = stacktop

for i in range(1,v+1):
  if(visited[i]==False):
    ans = -1
    break
    
    
print(ans)
  
    
  
  
  