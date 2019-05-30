#Snail algorith
#input int Y for square matrix size
#Algorithm fiils matrix with X^2 from 1 to Y
a = int(input())
m = [[0 for i in range(a)] for j in range(a)]
z = 1
x = 0
y = 0
p = 0
for q in range(a//2+1):
  #1st row
  # x=0 y=0
  for j in range(x,a-x):
    if z == a*a + 1:
      break
    m[0 + y][j] = z
    z += 1
  y += 1
  x += 1
  #right row
  #x=1 y=1 p=0
  for i in range(y,a-p):
    if z == a*a + 1:
      break
    m[i][a - x] = z
    z += 1
  #bot row
  #x=1 y=1
  for j in range(a - x - 1,-1+p,-1):
    if z == a*a + 1:
      break
    m[a-y][j] = z
    z += 1
  #left row
  x-=1
  # x=0 y=1
  for i in range(a - y - 1,0+p,-1):
    if z == a*a + 1:
      break
    m[i][x] = z
    z += 1
  y = q+1
  x = q+1
  p += 1
#output for m_res
nrows_m = len(m)
ncol_m = len(m[0])
for i in range (nrows_m):
  for j in range (ncol_m):
    print(str(m[i][j])+' ', end = '')
  print('')