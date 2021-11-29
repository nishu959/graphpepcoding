from heapq import heappop, heappush, heapify 

l = [] 
n = int(input())
for i in range(n):
  s = list(input().split())
  l.append(s)

graph = {}


for i in l:
  
  if i[0] not in graph:
    q = []
    heapify(q)
    heappush(q, i[1])
    graph[i[0]] = q
  
  else:
    t = graph[i[0]]
    heappush(t, i[1])
    graph[i[0]] = t
  
ans = []


def dfs(graph, ans, s):
  if s in graph:
    for i in range(len(graph[s])):
      a = graph[s]
      if(len(a)!=0):
        p = heappop(a) 
        dfs(graph, ans, p)
  
  ans.append(s)
  

dfs(graph, ans, "JFK")
print(ans[::-1])