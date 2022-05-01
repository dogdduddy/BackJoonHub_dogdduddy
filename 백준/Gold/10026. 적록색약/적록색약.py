import sys
sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline())

arr = [[] for _ in range(n)]
visited = [[0]*n for _ in range(n)]
visitedR = [[0]*n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cntR = 0
cnt = 0


def DFS(color, x, y):
    global cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[ny][nx] == 0 and color == arr[ny][nx]:
                visited[ny][nx] = 1
                DFS(color, nx, ny)

def DFSR(color, x, y):
    global cntR

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visitedR[ny][nx] == 0:
                if color == arr[ny][nx]:
                    visitedR[ny][nx] = 1
                    DFSR(color, nx, ny)
                elif (color == "R" or color == "G") and (arr[ny][nx] == "R" or arr[ny][nx] == "G"):
                    visitedR[ny][nx] = 1
                    DFSR(color, nx, ny)

for i in range(n):
    temp = sys.stdin.readline().strip()
    arr[i] = temp

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            DFS(arr[i][j], j, i)
            cnt += 1
for i in range(n):
    for j in range(n):
        if visitedR[i][j] == 0:
            DFSR(arr[i][j], j, i)
            cntR += 1
print(cnt, cntR)
