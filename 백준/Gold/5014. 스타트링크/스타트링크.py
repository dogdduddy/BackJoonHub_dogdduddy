# 최대 높이 F
# 현재 위치 S
# 목표 위치 G
# 위 U, 아래 D
from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [0]*(F+1)
bfs = deque()
ds = [U,D*-1]

def BFS():
    global G, F

    while bfs:
        now, num = bfs.popleft()

        if now == G:
            print(num)
            return

        for i in (0,1):
            ss = now + ds[i]
            if 0<ss<=F and visited[ss]==0:
                bfs.append((ss, num+1))
                visited[ss] = 1
    print("use the stairs")

bfs.append((S, 0))
visited[S] = 1
BFS()

