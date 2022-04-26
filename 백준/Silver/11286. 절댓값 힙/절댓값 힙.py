import sys
import heapq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    
    else:
        heapq.heappush(q,(abs(m),m))
