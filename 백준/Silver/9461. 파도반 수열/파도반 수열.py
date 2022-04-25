import sys

t = int(sys.stdin.readline())

p = [0,1,1,1,2,2,3] + [0]*95

for i in range(7,101):
    p[i] = p[i-1]+p[i-5]

for _ in range(t):
    n = int(sys.stdin.readline())
    print(p[n])