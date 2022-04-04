import sys

n, r, c = map(int, sys.stdin.readline().split())
cnt = 0
while n != 0:
    n -= 1
    if c < 2**n and r < 2**n:
        cnt += (2**n * 2**n)*0
    elif c >= 2**n and r < 2**n:
        cnt += (2**n * 2**n)*1
        c -= 2**n
    elif c < 2**n and r >= 2**n:
        cnt += (2**n * 2**n)*2
        r -= 2**n
    else:
        cnt += (2**n * 2**n)*3
        c -= 2**n
        r -= 2**n
print(cnt)
