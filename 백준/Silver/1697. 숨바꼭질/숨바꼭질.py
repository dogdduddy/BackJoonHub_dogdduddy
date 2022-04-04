from collections import deque

n, k = map(int, input().split())
q = deque([])
MAX = 100001
c = [0]*(MAX+1)

q.append(n)
def BFS():
    global k, MAX

    while q:
        num = q.popleft()
        if num == k:
            print(c[num])
            return
        for i in (num+1, num-1, num*2):
            if 0<=i<=MAX and not c[i]:
                c[i] = c[num]+1
                q.append(i)
BFS()
