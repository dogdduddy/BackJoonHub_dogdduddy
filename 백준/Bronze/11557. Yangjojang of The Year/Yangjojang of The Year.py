t = int(input())

for _ in range(t):
    n = int(input())
    arr = [[] for _ in range(n)]
    for i in range(n):
        arr[i] = list(input().split())
    Max = ("",0)
    for i in range(n):
        if int(Max[1]) < int(arr[i][1]):
            Max = arr[i]
    print(Max[0])
