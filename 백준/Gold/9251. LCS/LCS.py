import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

lena = len(a)
lenb = len(b)

arr = [[0]*(lenb+1) for _ in range(lena+1)]

for i in range(1, lena+1):
    for j in range(1, lenb+1):
        if a[i-1] == b[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])
print(arr[-1][-1])
