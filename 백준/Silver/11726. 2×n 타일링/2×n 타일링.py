n = int(input())

m = [0, 1, 2] + [0]*(n-2)

for i in range(3,n+1):
    m[i] = m[i-2] + m[i-1]
print(m[n]%10007)