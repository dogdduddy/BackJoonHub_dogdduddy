import sys
from collections import deque

m, n = map(int,sys.stdin.readline().split())

box = [0]*n
stack = deque()

for i in range(n):
    box[i] = list(map(int,sys.stdin.readline().split()))

px = [1, 0, -1, 0]
py = [0, 1, 0, -1]

# 시작 위치 선점 (Stack에 저장)

def BFS():
    while stack:
        x, y, cnt = stack.popleft()

        for j in range(4):
            dx = x + px[j]
            dy = y + py[j]
            if 0<=dx<m and 0<=dy<n and box[dy][dx] == 0:
                stack.append((dx, dy, cnt))
                box[dy][dx] = box[y][x] + 1
count = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            stack.append((j, i, 0))
        elif box[i][j] == 0:
            count+=1
if count == 0:
    print(0)
else:
    BFS()
    answer = 0
    for i in box:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(i))
    print(answer-1)