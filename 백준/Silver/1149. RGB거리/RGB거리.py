#참고 https://pacific-ocean.tistory.com/147
n = int(input())

m = []
for i in range(n):
    m.append(list(map(int, input().split())))
for i in range(1,n):
    m[i][0] = min(m[i-1][1], m[i-1][2]) + m[i][0]
    m[i][1] = min(m[i-1][0], m[i-1][2]) + m[i][1]
    m[i][2] = min(m[i-1][1], m[i-1][0]) + m[i][2]

print(min(m[n-1][0], m[n-1][1], m[n-1][2]))