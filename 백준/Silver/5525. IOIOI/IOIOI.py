import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

c = []
answer = 0
i = 0
cnt = 0
while i < m:
    if s[i:i+3] == "IOI":
        cnt += 1
        i+=2
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        cnt = 0
        i+=1

print(answer)
