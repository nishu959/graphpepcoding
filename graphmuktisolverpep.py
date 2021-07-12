import sys
from heapq import heappop, heappush, heapify


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
  

s = int(input())
d = int(input())

w = int(input())
k = int(input())

visited = [0]*v

mxm = -1*sys.maxsize
smxm = ""
mim = sys.maxsize 
smim = ""


cmax = sys.maxsize 
cpath = ""
fmin = -1*sys.maxsize 
fpath = ""


t = []
heapify(t)



def multisolver(graph, s, d, w, k, wsf, psf):
  global mxm, smxm, mim, smim, cmax, cpath, fmin, fpath, t
  if(s==d):
    
    if(wsf > mxm):
      mxm = wsf
      smxm = psf
      
    if(wsf < mim):
      mim = wsf
      smim = psf
      
    if(wsf > w and wsf < cmax):
      cmax = wsf
      cpath = psf
      
    if(wsf < w and wsf > fmin):
      fmin = wsf
      fpath = psf
     
    heappush(t, [wsf, psf]) 
    if(len(t)>k):
      heappop(t)
      
    
    return
    
  visited[s] = 1
  
  for i in graph[s]:
    if(visited[i.nbr] ==0):
      
      npsf = psf + str(i.nbr)
      nwsf = wsf + i.weigh
      
      multisolver(graph, i.nbr, d, w, k, nwsf, npsf)
      
  visited[s] = 0
  
  return 
  

multisolver(graph, s, d, w, k,0,"0")



print("Smallest Path = ", smim,"@", mim, sep ="")
print("Largest Path = ",smxm,"@", mxm, sep ="")
print("Just Larger Path than ", w," = ", cpath, "@",cmax, sep ="")
print("Just Smaller Path than ",w," = ", fpath, "@",fmin, sep ="")


print(k, "th largest path = ", t[0][1],"@", t[0][0],sep ="")

