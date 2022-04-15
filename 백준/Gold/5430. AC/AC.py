import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    check = True
    rever = False
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())

    if n != 0:
        arr = sys.stdin.readline().strip()[1:-1].split(',')
        q = deque(arr)
    else:
        input()
        q = []
        lenA = 0

    for i in p:
        if i =="R":
            if rever:
                rever = False
            else:
                rever = True
        elif i == "D":
            if len(q) == 0:
                print("error")
                check = False
                break
            else:
                if rever:
                    q.pop()
                else:
                    q.popleft()

    if check:
        if not rever:
            print("["+",".join(q)+"]")
        else:
            q.reverse()
            print("["+",".join(q)+"]")

