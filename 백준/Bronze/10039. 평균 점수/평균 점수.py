total = 0
for i in range(5):
    temp = int(input())
    if temp < 40:
        total += 40
    else:
        total += temp

print(total//5)
