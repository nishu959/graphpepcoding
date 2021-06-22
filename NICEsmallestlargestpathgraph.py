import sys 
from heapq import heappop, heappush, heapify

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
ip = int(input())
k = int(input())
t = []
heapify(t)

visited =[False]*v
minimum = sys.maxsize
maximum = -1 * sys.maxsize
spath = ""
mpath = ""
fpath = ""
cpath = ""
cmax= sys.maxsize
fmin = -1 * sys.maxsize


def haspath(graph, src, des, visited, psf, wt, ip, k):
  
  if(src == des):
    global minimum, spath, maximum, mpath, cmax, fmin, cpath, fpath, t
    if (wt<minimum):
      minimum = wt
      spath = psf 
      
    if(wt>maximum):
      maximum = wt
      mpath = psf
      
    if(wt>ip and wt<cmax):
      cmax = wt
      cpath = psf
      
    if(wt<ip and wt>fmin):
      fmin = wt
      fpath = psf
    
    heappush(t, [wt, psf])
    if(len(t)>k):
      heappop(t)
     
    return  
  
  visited[src] = True
  for child in graph[src]:
    if visited[child[1]]==False:
      haspath(graph, child[1], des, visited, psf + str(child[1]) , wt+child[2], ip, k)
  visited[src] = False
  return

haspath(graph, s, d, visited, "0", 0, ip, k)
  

print("Smallest Path = ", spath,"@", minimum, sep ="")
print("Largest Path = ",mpath,"@", maximum, sep ="")
print("Just Larger Path than ", ip," = ", cpath, "@",cmax, sep ="")
print("Just Smaller Path than ",ip," = ", fpath, "@",fmin, sep ="")


print(k, "th largest path = ", t[0][1],"@", t[0][0],sep ="")

