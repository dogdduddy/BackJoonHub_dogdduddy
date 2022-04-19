import sys
#Dynamic Programming

n = int(sys.stdin.readline())

dp = [0,1,3] + [0]*(n-2)

for i in range(3, n+1):
    if i%2 == 0:
        dp[i] = dp[i-1]*2 + 1
    else:
        dp[i] = dp[i-1]*2 - 1
print(dp[n]%10007)