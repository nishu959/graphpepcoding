class edge:
  def __init__(self, src, nbr):
    self.src = src
    self.nbr = nbr
    
n = int(input())
l = list(map(str, input().split()))
indegree = {}
graph = {}

for i in l:
  for j in i:
    indegree[j] = 0

flag = False    
con = 0
   
for i in range(len(l)-1):
  str1 = l[i]
  str2 = l[i+1]
  
  length = min(len(str1), len(str2))
  
  
  for p in range(length):
    ch1 = str1[p]
    ch2 = str2[p]
    
    if(ch1!=ch2):
      s = set()
      if ch1 in graph:
        s = graph[ch1]
        if ch2 not in s:
          s.add(ch2)
          indegree[ch2]+=1
          graph[ch1] = s
          
      else:
        s.add(ch2)
        indegree[ch2]+=1
        graph[ch1] = s
      
      flag = True
      break
      
  if(flag ==False and len(str1) > len(str2)):
    con = 1
    print("")



def kahn(graph, indegree):
  
  
  l = []
  
  for i in indegree:
    if(indegree[i]==0):
      l.append(i)
  
  
  idx = 0
  ans = ""
  
  while(len(l)>0):
    
    p = l.pop(0)
    
    ans += p
    
    idx+=1
    
    if p in graph:
      for k in graph[p]: 
        
     
        indegree[k]-=1
      
        if(indegree[k]==0):
          l.append(k)
  
  
 
 
  if(idx==len(indegree)):
    return ans
    
  else:
    return ""



if(con == 1):
  pass
else:
  print(kahn(graph, indegree))  

    