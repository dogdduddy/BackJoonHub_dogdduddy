import sys

n = int(sys.stdin.readline())
arr = [0]*20000000

temp = list(map(int,sys.stdin.readline().split()))
for i in temp:
    arr[i+10000000] = 1

m = int(sys.stdin.readline())
temp = list(map(int,sys.stdin.readline().split()))

for i in temp:
    print(arr[i+10000000], end=" ")
