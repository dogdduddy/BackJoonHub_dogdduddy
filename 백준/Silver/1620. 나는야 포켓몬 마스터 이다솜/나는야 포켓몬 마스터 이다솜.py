import sys

n, m = map(int, sys.stdin.readline().split())
book = {}

for i in range(n):
    book[sys.stdin.readline().strip()] = i+1
bookN = list(book.items())

for j in range(m):
    t = sys.stdin.readline().strip()
    if 48<=ord(t[0])<=57:
        print(bookN[int(t)-1][0])
    else:
        print(book[t])