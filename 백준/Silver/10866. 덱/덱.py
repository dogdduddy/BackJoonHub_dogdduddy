import sys
q = []

n = int(input())
for i in range(n):
    m = sys.stdin.readline().split()
    if "push_back" == m[0]:
        q.append(m[1])
    elif "push_front" == m[0]:
        q.insert(0, m[1])
    elif "front" == m[0]:
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif "back" == m[0]:
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
    elif "size" == m[0]:
        print(len(q))
    elif "empty" == m[0]:
        print(1 if len(q)==0 else 0)
    elif "pop_front" == m[0]:
        if len(q)==0:
            print(-1)
        else:
            print(q.pop(0))
    else:
        if len(q)==0:
            print(-1)
        else:
            print(q.pop())