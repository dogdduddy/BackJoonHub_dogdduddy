import sys
from collections import deque

m, n, h = map(int,sys.stdin.readline().split())

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]


tomato = [[[0]*m for _ in range(n)] for _ in range(h)]
Zerocnt = 0
bfs = deque()

def BFS():
    global n, m, h
    while bfs:
        z, y, x = bfs.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<m and 0<=ny<n and 0<=nz<h and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1
                bfs.append((nz,ny,nx))

for i in range(h):
    for j in range(n):
        for k, v in enumerate(map(int,sys.stdin.readline().split())):
            tomato[i][j][k] = v
            if v == 0:
                Zerocnt+=1
            elif v == 1:
                bfs.append((i,j,k))

if Zerocnt == 0:
    print(0)
else:
    BFS()
    answer = 0
    for i in range(h):
        for j in range(n):
            for k in tomato[i][j]:
                if k == 0:
                    print(-1)
                    exit(0)
                answer = max(answer, k)
    print(answer-1)
