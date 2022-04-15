import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

if m != 0:
    broken = list(sys.stdin.readline())
else:
    broken = []

answer = abs(100 - n)

for i in range(900901):
    for j in str(i):
        if j in broken:
            break
    else:
        answer = min(answer, len(str(i)) + abs(i-n))
print(answer)
