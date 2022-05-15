n, m = map(int, input().split())

s = dict()
cnt = 0

for i in range(n):
    s[input().strip()] = True

for j in range(m):
    check = input().strip()
    if check in s:
        cnt+=1

print(cnt)
