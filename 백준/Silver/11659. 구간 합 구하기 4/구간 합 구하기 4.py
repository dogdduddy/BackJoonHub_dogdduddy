import sys

n, m = map(int, sys.stdin.readline().split())
prefix = [0]

arr = list(map(int, sys.stdin.readline().split()))
temp = 0
for i in arr:
    temp += i
    prefix.append(temp)
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(prefix[e] - prefix[s-1])