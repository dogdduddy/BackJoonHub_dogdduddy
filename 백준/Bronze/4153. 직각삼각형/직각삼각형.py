import sys

while True:
    arr = list(map(int,sys.stdin.readline().split()))
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    Max = arr.pop(arr.index(max(arr)))
    temp = 0
    for i in arr:
        temp += i**2
    if Max**2 == temp:
        print("right")
    else:
        print("wrong")
