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
  

visited =[False]*v



def haspath(graph, src, des, visited, psf):
  
  if(src == des):
    print(psf)
    return 
  
  visited[src] = True
  for child in graph[src]:
    if visited[child[1]]==False:
      haspath(graph, child[1], des, visited, psf + str(child[1]))
  visited[src] = False
  

haspath(graph, s, d, visited, str(s) +"")
  

  

