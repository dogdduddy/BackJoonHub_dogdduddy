import sys
from collections import deque

t = int(sys.stdin.readline())

def BFS():
    while bfs:
        global v
        n, s = bfs.popleft()

        if n == v:
            print(s)
            break
        temp = (n*2)%10000
        if not visited[temp]:
            visited[temp] = True
            bfs.append((temp, s+"D"))

        temp = (n-1)%10000
        if not visited[temp]:
            visited[temp] = True
            bfs.append((temp, s+"S"))

        temp = ((n//1000)+n*10)%10000
        if not visited[temp]:
            visited[temp] = True
            bfs.append((temp, s+"L"))

        temp = ((n%10)*1000 + (n//10))%10000
        if not visited[temp]:
            visited[temp] = True
            bfs.append((temp, s+"R"))




for _ in range(t):
    n, v = map(int,sys.stdin.readline().split())
    bfs = deque()
    bfs.append((n, ""))
    visited = [False] * 10000
    visited[n] = True
    BFS()
