# 구현부
def DFS(t):
    visited[t] = True
    print(t, end=' ')
    for j in stack[t]:
        if not visited[j]:
            DFS(j)

def BFS(v):
    bfs = deque([v])
    visited[v] = True
    while bfs:
        t = bfs.popleft()
        print(t, end=' ')

        for i in stack[t]:
            if not visited[i]:
                bfs.append(i)
                visited[i] = True

import sys
from collections import deque

n, m, v = map(int,sys.stdin.readline().split())
stack = [[] for _ in range(n+1)]
visited = [False]*(n+1)

# 실행부
for _ in range(m):
    s, e = map(int,sys.stdin.readline().split())
    stack[s].append(e)
    stack[e].append(s)

# 낮은 번호 우선출력을 위한 정렬
for i in range(1,n+1):
    stack[i].sort()
#DFS
DFS(v)

print()
#BFS
visited = [False]*(n+1)
BFS(v)
