n = int(input())
s = input()

m = [0,0]
for i in s:
    if i == "A":
        m[0] += 1
    else:
        m[1] += 1
if m[0] > m[1]:
    print("A")
elif m[0] < m[1]:
    print("B")
else:
    print("Tie")
