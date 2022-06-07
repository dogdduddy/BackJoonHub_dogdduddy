# 5분 1분 10초
# 300 60 10
a = 300
b = 60
c = 10

cnt = [0,0,0]

n = int(input())
cnt[0] += n//a
n = n%a
cnt[1] += n//b
n = n%b
cnt[2] += n//c
n = n%c

if n > 0:
    print(-1)
else:
    print("{} {} {}".format(cnt[0], cnt[1], cnt[2]))
