import sys
import heapq

n = int(sys.stdin.readline().strip())
q = []


for i in range(n):
    m = int(sys.stdin.readline().strip())
    if m == 0:
        if not len(q):
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (-m, m))