import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(n)]
cnt = [0]*n
stack = deque()

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    tree[s-1].append(e-1)
    tree[e-1].append(s-1)

def BFS(s, t):

    stack.append(s)
    cnt[s] = t

    while stack:
        e = stack.popleft()
        for i in tree[e]:
            if not cnt[i]:
                stack.append(i)
                cnt[i] = t
t = 0
for i in range(n):
    if not cnt[i]:
        t += 1
        BFS(i, t)
print(t)
