class edge():
  def __init__(self, src, nbr, weigh):
    self.src = src
    self.nbr = nbr
    self.weigh = weigh
   
  
v = int(input())
e = int(input())

graph = {}

for i in range(v):
  graph[i] = []
  
  
for i in range(e):
  a, b, c = map(int, input().split())
  graph[a].append(edge(a, b, c))
  graph[b].append(edge(b, a, c))  
  



visited = [0]*v

ans = []



def getconcom(graph, src, ele, visited):
  visited[src] = 1
  
  #ele.append(src) this will also work
  #in this case we have to pass empty list not with first element
  
  for i in graph[src]:
    if(visited[i.nbr]==0):
      
      ele.append(i.nbr)
      getconcom(graph, i.nbr, ele, visited)
    

for i in range(v):
  if(visited[i]==0):
    ele = [i]
    
    getconcom(graph, i, ele , visited)
    
    ans.append(ele)
    
    
       
print(ans)



