import sys
import heapq

q = []

n = int(sys.stdin.readline().strip())
for i in range(n):
    m = int(sys.stdin.readline().strip())
    if m == 0:
        if not len(q):
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,m)
