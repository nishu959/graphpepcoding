class edge:
  
  def __init__(self, src, nbr):
    self.src = src
    self.nbr = nbr  

graph = {}

v, e = map(int, input().split())

for i in range(v):
  graph[i] = []
  
 
for i in range(e):
  
  a, b= map(int, input().split())
  graph[b].append(edge(b, a))
  

indegree = [0]*(v)

for i in range(v):
  for j in graph[i]:
    indegree[j.nbr]+=1
 

  
def kahn(graph, indegree):
  
  l = []
  
  for i in range(len(graph)):
    if(indegree[i]==0):
      l.append(i)
  
  
  
  idx = 0
  ans = []
  
  while(len(l)>0):
    
    p = l.pop(0)
    ans.append(p)    
    
    idx+=1
    
    for k in graph[p]: 
     
      indegree[k.nbr]-=1
      
      if(indegree[k.nbr]==0):
        l.append(k.nbr)
  
  
 
  
  if(idx==len(graph)):
    return ans
    
  else:
    return [-1]
    
    

p =kahn(graph, indegree)
print(*p)



