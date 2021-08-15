
class edge:
  def __init__(self, src, nbr):
    self.src = src
    self.nbr = nbr
   
 

def sdfs(graph, visited, stack, s):
  
  visited[s] = True
  
  for i in graph[s]:
    
    if(visited[i]==False):
      sdfs(graph, visited, stack, i)
      
  stack.append(s)
  
  
 
def transpose(graph):
  
  result = {}
  for i in range(1,v+1):
    result[i] = []
  
  
  for i in range(1,v+1):
    for j in graph[i]:
      result[j].append(i)
      
  return result
  
  
def dfs(g, visited, s):
  
  visited[s] = True
  
  for i in g[s]:
    
    if(visited[i]==False):
      dfs(g, visited, i)
      
  
      
      
  

v, e = map(int, input().split())
graph = {}

for i in range(1,v+1):
  graph[i] = []
  
  
for i in range(e):
  a, b =map(int, input().split())
  
  graph[a].append(b)
  

visited = [False]*(v+1)
stack = []

for i in range(1,v+1):
  if(visited[i]==False):
    sdfs(graph, visited, stack, i)
    
    

result = transpose(graph)
count = 0

visited = [False]*(v+1)



while(len(stack)>0):
  
  cur = stack.pop()
  
  if(visited[cur]==False):
    
    dfs(result, visited, cur)
    count += 1
    
    
print(count)

    
    

    
    

