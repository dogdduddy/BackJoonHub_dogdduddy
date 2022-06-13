t = input()

left = 0
right = len(t)-1

while left < right:
    if t[left] != t[right]:
        print(0)
        break
    left += 1
    right -= 1
if left >= right:
    print(1)
