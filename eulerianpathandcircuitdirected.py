#if indegree == outdegree(for every index) 
# then Eulerian circuit 

#if outdegree == indegree(n-2 times) and
#outdegree + 1 = indegree and indegree + 1 = outdegree
#then Eulerian path


v, e = map(int, input().split())

graph = {}

for i in range(v):
  graph[i] = []
 

for i in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
 


indegree = [0]*v

outdegree = [0]*v

for i in range(v): 
  for j in graph[i]:
    outdegree[i]+=1
    indegree[j]+=1
    
    

if(indegree ==outdegree ):
  print("Eulerian circuit")
  print("Eulerian path")
 

same = 0
diff = 0 

for i in range(len(indegree)):
  if(indegree[i] == outdegree[i]):
    same += 1
    
  elif(indegree[i] + 1 == outdegree[i]):
    diff += 1
    
  elif(outdegree[i] + 1 ==indegree[i]):
    diff += 1
    

if(same == v-2 and diff == 2):
  print("Eulerian path")
  

    
    
    


