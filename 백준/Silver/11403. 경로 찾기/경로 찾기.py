import sys

n = int(sys.stdin.readline())

arr = [[0]*n for _ in range(n)]
line = [[] for _ in range(n)]
dfs = []
visited = [0]*n

for i in range(n):
    m = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if m[j] == 1:
            line[i].append(j)

def DFS(s):
    temp = line[s]
    for i in temp:
        if not visited[i]:
            visited[i] = 1
            dfs.append(i)
            DFS(i)

for i in range(n):
    visited = [0]*n
    DFS(i)
    for j in dfs:
        arr[i][j] = 1
    dfs.clear()

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
