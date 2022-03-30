import sys

n = int(input())
arr = [0]*20000001

for i in list(map(int,sys.stdin.readline().split())):
    arr[i+10000000] += 1

m = int(input())
for i in list(map(int,sys.stdin.readline().split())):
    print(arr[i+10000000], end=" ")