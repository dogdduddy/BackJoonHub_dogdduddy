import sys
sys.setrecursionlimit(100000)

n, m, r = map(int, input().split())

visited = [0]*(n+1)
tree = [[] for _ in range(n+1)]
cnt = 1

for i in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(1, n+1):
    tree[i].sort()

def dfs(t, r):
    global cnt
    visited[r] = cnt
    cnt += 1

    for i in t[r]:
        if visited[i] == 0:
            dfs(t, i)

dfs(tree, r)
for i in range(1,n+1):
    print(visited[i])
