import sys
n = int(sys.stdin.readline())
nA = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mA = list(map(int,sys.stdin.readline().split()))

for i in mA:
    if i in nA:
        print(1)
    else:
        print(0)
