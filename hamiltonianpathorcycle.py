v = int(input())
e = int(input())

graph = {}
for i in range(v):
  graph[i] = []
 
for i in range(e):
  l =list(map(int, input().split()))
  graph[l[0]].append([l[0],l[1],l[2]])
  graph[l[1]].append([l[1],l[0],l[2]])
 

s = int(input())
visited = [0]*v
#print(graph)


def hamilton(graph, src, psf, visited, initial):
  if(len(psf)==len(visited)) :
    edge = False
    for i in graph[src]:
      if(i[1]==initial):
        edge = True
        break
    if(edge):
      print(psf+"*")
    else:
      print(psf+".")
    return
  visited[src] = 1
  
  for child in graph[src]:
    if(visited[child[1]] ==0):
      hamilton(graph, child[1], psf+str(child[1]),visited, initial)
  visited[src] =0
      
hamilton(graph, s, str(s), visited, s)





  