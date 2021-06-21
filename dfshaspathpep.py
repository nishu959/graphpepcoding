v = int(input())
e = int(input())
graph = {}

for i in range(v):
  graph[i] = []
for i in range(e):
  l = list(map(int, input().split())) 
  graph[l[0]].append([l[0],l[1],l[2]]) 
  graph[l[1]].append([l[1],l[0],l[2]])
  
s =int(input())
d = int(input())
  

visited = [0]*v



def haspath(graph, src, des, visited):
  if(src == des):
    return True
  visited[src] = 1
  for child in graph[src]:
    if visited[child[1]]==0:
      path = haspath(graph, child[1], des, visited)
      if path ==True:
        return True
  
  
  
  return False



if(haspath(graph, s, d, visited)):
  print("true")
else:
  print("false")

