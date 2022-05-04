import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

cnt = 100
arr = [0]*(n+m)

for i in range(n+m):
    arr[i] = list(map(int,sys.stdin.readline().split()))

visited = [1]*101
bfs = deque()

def BFS():
    global cnt
    while bfs:
        n, loc = bfs.popleft()
        if loc == 100:
            cnt = min(cnt, n)
            return

        for i in range(1,7):
            temp = loc + i
            if temp <= 100 and visited[temp]:
                for j in arr:
                    if temp == j[0]:
                        visited[j[1]] = 0
                        bfs.append((n+1,j[1]))
                        break
                else:
                    visited[temp] = 0
                    bfs.append((n+1,temp))

bfs.append((0,1))
BFS()
print(cnt)
