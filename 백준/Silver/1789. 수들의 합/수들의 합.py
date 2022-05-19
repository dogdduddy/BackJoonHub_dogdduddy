s = int(input())

Sum = 0
cnt = 0

for i in range(1,s+1):
    Sum += i
    cnt += 1
    if s == Sum:
        print(cnt)
        break
    elif s < Sum:
        print(cnt-1)
        break