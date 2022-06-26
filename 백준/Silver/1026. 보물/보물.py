n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

temp = []
for i in range(len(b)):
    temp.append((i, b[i]))

temp = sorted(temp, key=lambda x:x[1])
a.sort(reverse=True)
total = 0
print(sum(a[i]*temp[i][1] for i in range(len(a))))
