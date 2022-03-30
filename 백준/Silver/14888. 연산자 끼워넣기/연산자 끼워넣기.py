import sys

n = int(sys.stdin.readline())

num = list(map(int,sys.stdin.readline().split()))
inp = list(map(int,sys.stdin.readline().split()))

ope = []
save = []

temp = {0:"+", 1:"-", 2:"*", 3:"/"}
for i in range(len(inp)):
    for j in range(inp[i]):
        ope.append(temp[i])

sumMax = -1000000000
sumMin = 1000000000

def DFS(cnt):
    global sumMax, sumMin

    if cnt == n:
        total = num[0]
        for i in range(len(save)):
            if save[i] == "+":
                total += num[i+1]
            elif save[i] == "-":
                total -= num[i+1]
            elif save[i] == "*":
                total *= num[i+1]
            else:
                total = int(total / num[i+1])
        sumMax = max(sumMax, total)
        sumMin = min(sumMin, total)
        return

    for i in range(len(ope)):
        save.append(ope.pop(i))
        DFS(cnt+1)
        ope.insert(i, save.pop())

DFS(1)
print(sumMax)
print(sumMin)
