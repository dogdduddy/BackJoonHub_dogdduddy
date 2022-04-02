import sys
t = int(sys.stdin.readline())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
# 재귀 대신 스택으로 구현해보기

def DFS(x, y):
    s = [[x, y]]
    while s:
        x, y = s[0][0], s[0][1]
        del s[0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx]==1:
                maps[ny][nx] = 0
                s.append((nx, ny))

for k in range(t):
    m, n, k = list(map(int, sys.stdin.readline().split()))
    maps = [[0]*m for _ in range(n)]

    for _ in range(k):
        input1, input2 = map(int, sys.stdin.readline().split())
        maps[input2][input1] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                cnt += 1
                maps[i][j] = 0
                DFS(j, i)
    print(cnt)
