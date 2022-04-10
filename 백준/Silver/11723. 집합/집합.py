import sys
n = int(sys.stdin.readline())

s = set()
temp = set()

for _ in range(n):
    m = sys.stdin.readline().split()
    if len(m) == 1:
        if m[0] == "all":
            s = {i for i in range(1,21)}
        elif m[0] == "empty":
            s.clear()
    else:
        com = m[0]
        v = int(m[1])

        if com == "add":
            s.add(v)
        elif com == "remove":
            s.discard(v)
        elif com == "check":
            if v in s:
                print(1)
            else:
                print(0)
        elif com == "toggle":
            if v in s:
                s.discard(v)
            else:
                s.add(v)




