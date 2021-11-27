class edge:
  def __init__(self, src, nbr, wt):
    self.src = src
    self.nbr = nbr
    self.wt = wt
   
  def __lt__(self, nxt):
    return self.wt < nxt.wt 
    
    
v = int(input())
e = int(input()) 
l = []

for i in range(e):
  a, b, c = map(int, input().split())
  l.append(edge(a, b, c))

l.sort()
par = [i for i in range(v)]
rank = [1 for i in range(v)]

def find(x):
  if(par[x]==x):
    return x
  temp = find(par[x])
  par[x] = temp
  return temp
  
def union(x, y):
  lx = find(x)
  ly = find(y)
  if(lx!=ly):
    if(rank[lx]>rank[ly]):
      par[ly] = lx
    elif(rank[lx]<rank[ly]):
      par[lx] = ly
    else:
      par[lx] = y
      rank[ly]+=1
    
    return True  
  return False

ans = 0 

for i in l:
  boolunion = union(i.src,i.nbr)
  if(boolunion):
    ans += i.wt
    

print(ans)

  