import sys

n = int(sys.stdin.readline())
m = [[] for _ in range(n)]

for i in range(n):
    m[i] = list(map(int, list(sys.stdin.readline().strip())))

answer = ""

def dfs(x,y,n):
    global answer
    temp = m[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if m[i][j] != temp:
                answer += "("
                for k in range(2):
                    for l in range(2):
                        dfs(x+l*(n//2), y+k*(n//2), n//2)
                answer += ")"
                return
    if temp == 1:
        answer += "1"
    elif temp == 0:
        answer += "0"

dfs(0,0,n)
print(answer)