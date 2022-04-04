n = list(map(int, input().split()))
SUM = 0
for i in range(5):
    SUM += n[i]**2
print(SUM%10)
