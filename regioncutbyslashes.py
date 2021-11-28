n = int(input())
l = []
for i in range(n):
  s = input()
  
  l.append(s)
  
cell = (n+1)*(n+1)
par = [i for i in range(cell)]

rank = [1 for i in range(cell)]

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
 
for i in range(n+1):
  for j in range(n+1):
    if(i==0 or j==0 or i==n or j==n):
      t = i * (n+1) + j
      union(0,t)
      
region = 1
for i in range(n):
  for j in range(n):
    
    if l[i][j]=="/":
      cell1 = i * (n+1) + (j+1)
      cell2 = (i+1)* (n+1) + (j)
      boola = union(cell1,cell2)
      if(boola ==False):
        region += 1
    elif l[i][j]=="\\":
      cell1 = i * (n+1) + (j)
      cell2 = (i+1)* (n+1) + (j+1)
      boolb = union(cell1,cell2)
      if(boolb ==False):
        region += 1
    else:
      continue
      
print(region)
      
    
    
    
      
      

    
    


