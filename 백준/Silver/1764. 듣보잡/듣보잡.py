import sys
n, m = map(int, sys.stdin.readline().split())
a = []
b = []

for i in range(n):
    a.append(sys.stdin.readline().strip())
for i in range(m):
    b.append(sys.stdin.readline().strip())

c = list(set(a) & set(b))

print(len(c))
c.sort()
for i in c:
    print(i)
