import sys

n = int(sys.stdin.readline())

m = list(map(int,sys.stdin.readline().split()))
mSet = list(set(m))
mSet.sort(reverse=True)

arr = {}
for i in range(len(mSet)):
    arr[mSet[i]] = len(mSet) - i - 1

for i in m:
    print(arr[i])