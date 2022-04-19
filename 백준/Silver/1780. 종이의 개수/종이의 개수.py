import sys
# DFS, BFS

def check(x, y, s):
    temp = paper[y][x]
    for i in range(y,y+s):
        for j in range(x,x+s):
            if paper[i][j] != temp:
                return False
    return True

def tree(x, y, n):
    step = n//3

    if n == 1:
        cnt[paper[y][x]] += 1
        return

    for i in range(3):
        for j in range(3):
            if check(x+j*step,y+i*step,step):
                cnt[paper[y+i*step][x+j*step]] += 1
            else:
                tree(x+j*step,y+i*step,step)

n = int(sys.stdin.readline())
paper = [[] for _ in range(n)]
cnt = {-1:0, 0:0, 1:0}

if n==1:
    cnt[int(sys.stdin.readline())] += 1
else:
    for i in range(n):
        paper[i] = list(map(int,sys.stdin.readline().split()))
    temp = paper[0][0]
    c = True
    for i in range(n):
        for j in range(n):
            if paper[i][j] != temp:
                c = False
    if c:
        cnt[temp] += 1
    else:
        tree(0, 0, n)
print(cnt[-1])
print(cnt[0])
print(cnt[1])
