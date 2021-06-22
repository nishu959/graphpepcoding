def haspath(graph, src, ele,visited):
  visited[src] = 1
  
  ele.append(src)
   
  for child in graph[src]:
    if visited[child[1]]==0:
      
      haspath(graph, child[1],ele, visited)
      
      
  
      


v = int(input())
e = int(input())
graph = {}

for i in range(v):
  graph[i] = []
for i in range(e):
  l = list(map(int, input().split())) 
  graph[l[0]].append([l[0],l[1],l[2]]) 
  graph[l[1]].append([l[1],l[0],l[2]])
 
visited = [0]*v
p = []
for i in range(v):
  if visited[i]==0:
    ele = []
    haspath(graph, i,ele, visited)
    p.append(ele) 
   
  


print(p)

