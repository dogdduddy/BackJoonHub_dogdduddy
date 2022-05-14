n, w, h = map(int, input().split())
for _ in range(n):
    t = int(input())
    if t <= (w**2 + h**2) ** 0.5:
        print("DA")
    else:
        print("NE")
