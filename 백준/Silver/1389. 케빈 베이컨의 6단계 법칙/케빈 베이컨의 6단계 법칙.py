from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
total = (50000, 0)
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


def BFS(t):
    cnt = 0
    visited[t] = 1

    for i in arr[t]:
        bfs.append((i,1))

    while bfs:
        idx, count = bfs.popleft()
        if visited[idx] == 1:
            continue
        visited[idx] = 1
        cnt += count

        for i in arr[idx]:
            if visited[i] == 0:
                bfs.append((i,count+1))
    return (cnt, t)

for i in range(1,n+1):
    visited = [0]*(n+1)
    bfs = deque()
    temp = BFS(i)
    total = temp if total[0] > temp[0] else total
print(total[1])
