class edge():
  def __init__(self, src, nbr, weigh):
    self.src = src
    self.nbr = nbr
    self.weigh = weigh
   
  
graph= {}
v = int(input())
e = int(input())

for i in range(v):
  graph[i] = []
  

for i in range(e):
  a, b, c = map(int, input().split())
  graph[a].append(edge(a, b, c))
  graph[b].append(edge(b, a, c))
  
  
  
def concomps(graph, s,ele , visited):
  
  visited[s] = 1
  
  
  for i in graph[s]:
    if(visited[i.nbr] ==0):
      ele.append(i.nbr)
      concomps(graph, i.nbr,ele ,visited)
      
 
 
visited = [0]*v
ans = []
   
for j in range(v):
  if(visited[j]==0):
    ele = [j]
    concomps(graph, j,ele ,visited)
    ans.append(ele)
    
    
    
print("true") if(len(ans)==1) else print("false")
      
  
  
 

