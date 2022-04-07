import sys

n = int(sys.stdin.readline().strip())

dp = [0]*301
inp = [0]*301

for i in range(n):
    inp[i] = int(sys.stdin.readline().strip())
dp[0] = inp[0]
dp[1] = dp[0] + inp[1]
dp[2] = max(inp[0]+inp[2], inp[1]+inp[2])

for i in range(3,n):
    dp[i] = max(dp[i-3] + inp[i-1] + inp[i], dp[i-2] + inp[i])
print(dp[n-1])
