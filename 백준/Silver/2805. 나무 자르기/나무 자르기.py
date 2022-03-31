import sys
n, m = map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))

top = max(tree)
bottom = 1
total = 0

while bottom <= top:
    mid = (top+bottom)//2
    total = 0
    for i in range(n):
        if tree[i] > mid:
            total +=  tree[i] - mid
    if total >= m:
        bottom = mid + 1
    else:
        top = mid - 1
print(top)


