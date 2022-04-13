import sys
import heapq

t = int(sys.stdin.readline().strip())
for _ in range(t):
    k = int(sys.stdin.readline().strip())
    visited = [0]*1000001
    up = []
    down = []
    for i in range(k):
        d, n = sys.stdin.readline().split()
        n = int(n)
        if d == "I":
            heapq.heappush(up, (-n, i))
            heapq.heappush(down, (n, i))
            visited[i] = 1
        elif d == "D":
            if n == 1 :
                while up and not visited[up[0][1]]:
                    heapq.heappop(up)
                if up:
                    visited[up[0][1]] = 0
                    heapq.heappop(up)

            elif n == -1:
                while down and not visited[down[0][1]]:
                    heapq.heappop(down)
                if down:
                    visited[down[0][1]] = 0
                    heapq.heappop(down)

    while down and not visited[down[0][1]]:
        heapq.heappop(down)
    while up and not visited[up[0][1]]:
        heapq.heappop(up)

    if down and up:
        print(-up[0][0], down[0][0])
    else:
        print("EMPTY")

