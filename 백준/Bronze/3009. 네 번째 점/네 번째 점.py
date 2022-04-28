import sys

X = []
Y = []

for _ in range(3):
    x, y = map(int,sys.stdin.readline().split())
    if not x in X:
        X.append(x)
    else:
        X.remove(x)

    if not y in Y:
        Y.append(y)
    else:
        Y.remove(y)
print(X.pop(), Y.pop())