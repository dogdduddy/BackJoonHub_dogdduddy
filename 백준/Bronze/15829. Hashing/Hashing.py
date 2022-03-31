n = int(input())
m = input()

answer = 0
for i in range(n):
    answer += ((ord(m[i])-96)*(31**i)) 

print(answer% 1234567891)