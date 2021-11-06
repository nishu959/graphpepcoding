l = []
for i in range(2):
  l.append(list(map(int, input().split())))
  
target = "123450"
start = ""

for i in l:
  for j in i:
    start += str(j)
    
swix = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]

queue = []

queue.append(start)
level = -1
visited = set()

def fun(string, i, a):
  
  k = list(string)
  res = k[i]
  k[a] = res
  k[i] = "0"
  ans = "".join(k)
  
  return ans
  
flag = False 
while(len(queue)>0):
  if(flag):
    break
  level += 1
  size = len(queue)
  
  while(size>0):
    t = queue.pop(0)
    
    if(t==target):
      flag = True
      break
    a =-1 
    for i in range(6):
      if(t[i]=="0"):
        a = i
    arr = swix[a]
    for i in arr:
      ans = fun(t, i, a)
      
      if ans not in visited:
        visited.add(ans) 
        queue.append(ans)
    
    size -= 1
  
if(flag):
  print(level)
else:
  print(-1)
