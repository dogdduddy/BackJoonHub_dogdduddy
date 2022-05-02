import sys

n = int(sys.stdin.readline())

dp = [0, 1]+[0]*(n-1)

for i in range(2,n+1):
    m = 50001
    j = 1
    while (j**2) <= i:
        m = min(m, dp[i-(j**2)])
        j += 1
    dp[i] = m+1
print(dp[n])
