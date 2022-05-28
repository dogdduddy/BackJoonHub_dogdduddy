import sys
from collections import deque

n = int(sys.stdin.readline())
board = [[] * n for _ in range(n)]
MaxSize = 0
bfs = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().split()))
    MaxSize = max(MaxSize, max(board[i]))


def BFS():
    while bfs:
        x, y = bfs.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                bfs.append((nx, ny))


Max = 0
for i in range(0, MaxSize):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if board[j][k] <= i:
                visited[j][k] = 1

    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0:
                bfs.append((k, j))
                BFS()
                cnt += 1
    Max = max(Max, cnt)

print(Max)
