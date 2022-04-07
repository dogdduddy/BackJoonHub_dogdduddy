import sys
n, m = map(int, sys.stdin.readline().split())

www = {}

for i in range(n):
    site, pw = sys.stdin.readline().split()
    www[site] = pw


for i in range(m):
    print(www[sys.stdin.readline().strip()])
