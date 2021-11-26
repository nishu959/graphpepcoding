class edge:
  def __init__(self, typeof, src, nbr):
    self.typeof = typeof
    self.src = src
    self.nbr = nbr
  
  
v, e = map(int, input().split())

  
graph = []


for i in range(e):
  t, a, b = map(int, input().split())
  graph.append(edge(t, a, b))
  

paralice = [i for i in range(v+1)]
parbob = [i for i in range(v+1)]
rankalice = [1 for i in range(v+1)]
rankbob =[1 for i in range(v+1)] 


def find(x, parent):
  if(parent[x]==x):
    return x
  temp = find(parent[x], parent)
  parent[x] = temp
  return temp
  
def union(x, y, parent, Rank):
  lx = find(x, parent)
  ly = find(y, parent)
  if(lx!=ly):
    if(Rank[lx]>Rank[ly]):
      parent[ly] = lx
    elif(Rank[lx]<Rank[ly]):
      parent[lx] = ly
    else:
      parent[lx] = y
      Rank[ly]+=1
    
    return True  
  return False
    

countalice = 1
countbob = 1
remove = 0   
   
for j in graph:
  if j.typeof==3:
    boola = union(j.src,j.nbr, paralice, rankalice)
    boolb = union(j.src,j.nbr, parbob, rankbob)
      
    if(boola):
      countalice += 1
      
    if(boolb):
      countbob += 1
        
    if(boola==False and boolb==False):
      remove += 1
        
        

for j in graph:
  if j.typeof==1:
    boola = union(j.src,j.nbr, paralice, rankalice)
    if(boola):
      countalice += 1
    else:
      remove += 1
  if(j.typeof==2):
    boolb = union(j.src,j.nbr, parbob, rankbob)
    if(boolb):
      countbob += 1
    else:
      remove += 1
    
        
if(countbob==countalice==v):
  print(remove)
  


else:
  print(-1)
      
      
    
    
    
    