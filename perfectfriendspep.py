class edge():
  def __init__(self, src, nbr):
    self.src = src
    self.nbr = nbr
   
  
v = int(input())
e = int(input())

graph = {}

for i in range(v):
  graph[i] = []
 

for i in range(e):
  a, b = map(int, input().split())
  graph[a].append(edge(a, b))
  graph[b].append(edge(b, a))
 

visited = [0]*v


def concom(graph, s, visited, ele):
  visited[s] = 1
  for i in graph[s]:
    if(visited[i.nbr] == 0):
      ele.append(i.nbr)
      concom(graph, i.nbr, visited, ele)
      
      
  
  
ans = [] 
  
for i in range(v):
  if(visited[i]==0):
    ele = [i]
    concom(graph, i, visited, ele)
    ans.append(ele)
    
answer = 0    


for i in range(len(ans)):
  p = len(ans[i])
  
  for j in range(i+1,len(ans)):
    answer += p * len(ans[j])
    
    
    
print(answer)
    
  
    
  