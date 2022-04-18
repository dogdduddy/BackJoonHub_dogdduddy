import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    wet = {}
    for _ in range(n):
        m, k = sys.stdin.readline().split()
        if k in list(wet.keys()):
            wet[k] += 1
        else:
            wet[k] = 1

    lis = list(wet.values())
    temp = 1
    for i in lis:
        temp *= (i+1)
    print(temp - 1)
