n = int(input())
l = list(map(int, input().split()))

class pair:
  def __init__(self, data, index):
    self.data = data
    self.index = index
   
  def __lt__(self,other):
    return self.data<other.data
    

t = []  
for i in range(n):
  t.append(pair(l[i],i))
  
t.sort()

 
vis = [None]*(n+1)
ans = 0

for i in range(n):
  if(vis[i]==1 or t[i].index==i):
    continue
    
  cycle = 0
  j = i
  while(vis[j]==None):
    vis[j] = 1
    cycle += 1
    j = t[j].index
    
  ans += cycle-1
  
print(ans)
  
  
  
  