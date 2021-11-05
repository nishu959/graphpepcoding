m = int(input())
n = int(input())
l = []
for i in range(m):
  l.append(list(map(int, input().split())))
 
src, des = map(int, input().split())

d = {}
for i in range(m):
  for j in range(len(l[i])):
    d[l[i][j]] = []

for i in range(m):
  for j in range(len(l[i])):
    d[l[i][j]].append(i)
   
  
queue = []
b_s_v = set()
b_n_v = set()

queue.append(src)
b_s_v.add(src)


level = -1
flag= False

while(len(queue)>0):
  if(flag):
    break
  size = len(queue)
  level +=1
  while(size>0):
    p = queue.pop(0)
    if(p==des):
      flag = True
      break
       
    bustogo = d[p]
    for i in bustogo:
      if i in b_n_v:
        continue
      busstoptogo = l[i]
      for j in busstoptogo:
        if j in b_s_v:
          continue
        
        queue.append(j)
        b_s_v.add(j)
        
      b_n_v.add(i)

    size -= 1
    
  
if(flag):
  print(level)
else:
  print(-1)