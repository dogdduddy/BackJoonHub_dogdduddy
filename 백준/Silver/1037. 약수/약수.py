import sys
n = int(sys.stdin.readline())
m = [0]*n
m = list(map(int,sys.stdin.readline().split()))
print(max(m)*min(m))