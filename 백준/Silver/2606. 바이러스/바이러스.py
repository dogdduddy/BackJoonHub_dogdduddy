import sys

n = int(sys.stdin.readline().strip())
l = int(sys.stdin.readline().strip())

m = [[] for _ in range(n)]

com = [0]*n

for i in range(l):
    s, t = map(int, sys.stdin.readline().split())
    m[s-1].append(t-1)
    m[t-1].append(s-1)
cnt = 0

def DFS(index):
    global n, cnt
    com[index] = 1
    for i in m[index]:
        if not com[i]:
            com[i] = 1
            cnt += 1
            DFS(i)
DFS(0)
print(cnt)
