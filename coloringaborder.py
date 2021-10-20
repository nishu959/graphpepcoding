dir = [[0,1],[1,0],[0,-1],[-1,0]]

def dfs(grid, row, col, clr):
  
  grid[row][col] = -clr
  count = 0
   
  
  
  for i in range(4):
    row_ = row + dir[i][0]
    col_ = col + dir[i][1]
    
   
    if(row_ <0 or col_ <0 or row_ >= len(grid) or col_>=len(grid[0]) or abs(grid[row_][col_])!=clr):
      continue
    
    count += 1
    
    
    if(grid[row_][col_] == clr):
      dfs(grid, row_, col_, clr)
      
  if(count == 4):
    grid[row][col] = clr
    
    
      
    
row = int(input())
col = int(input())
grid = []

for i in range(row):
  grid.append(list(map(int, input().split())))
  


R = int(input())
C = int(input())
 

color = int(input())



dfs(grid, R, C, grid[R][C])


for i in range(len(grid)):
  for j in range(len(grid[0])):
    
    if(grid[i][j]<0):
      grid[i][j] = color
      
      
print(grid)







