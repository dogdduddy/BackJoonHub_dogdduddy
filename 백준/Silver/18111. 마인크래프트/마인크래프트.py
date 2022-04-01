import sys
n, m, b = map(int,sys.stdin.readline().split())

area = []
for i in range(n):
    area.append(list(map(int,sys.stdin.readline().split())))

cnt = 1000000000000000000000000000000
heigh = 0

for h in range(257):
    max = 0
    min = 0
    for i in range(n):
        for j in range(m):
            temp = area[i][j]
            if temp < h:
                min += h - temp
            else:
                max += temp - h
    inv = max + b
    if inv < min:
        continue
    time = 2*max + min
    if time <= cnt:
        cnt = time
        heigh = h

print(cnt, heigh)