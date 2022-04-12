import sys

n = int(sys.stdin.readline().strip())
m = [0]*n

pattonX = [1, 0, 1, 0]
pattonY = [1, 1, 0, 0]

cntB, cntW = 0, 0

for i in range(n):
    m[i] = list(map(int,sys.stdin.readline().split()))

def DFS(x, y):
    global cntB, cntW

    sx, ex = x
    sy, ey = y
    midx = (sx + ex) // 2
    midy = (sy + ey) // 2

    if ex - sx == 1 or check((sx, ex), (sy, ey)):
        if m[sy][sx] == 1:
            cntB += 1
        else:
            cntW += 1
        return

    for i in range(4):
        x[pattonX[i]] = midx
        y[pattonY[i]] = midy
        DFS(x, y)
        x = [sx, ex]
        y = [sy, ey]

def check(x, y):
    temp = m[y[0]][x[0]]
    for i in range(y[0],y[1]):
        for j in range(x[0],x[1]):
            if temp != m[i][j]:
                return False
    return True

DFS([0,n],[0,n])
print(cntW)
print(cntB)

