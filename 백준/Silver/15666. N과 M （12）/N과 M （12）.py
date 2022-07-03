# N개의 자연수와 자연수 M
# 길이가 M인 수열을 모두 구하여라

# N개의 자연수 중에서 M개를 고른 수열
# 중복 가능
# 비내림차순으로

N, M = map(int, input().split())
numbers = []
for i in list(map(int,input().split())):
    if not i in numbers:
        numbers.append(i)
numbers.sort()
arr = []

def DFS(cnt):
    global M
    if cnt == M:
        for i in arr:
            print(i, end=" ")
        print()
        return
    for i in numbers:
        if cnt == 0 or arr[-1] <= i:
            arr.append(i)
            DFS(cnt+1)
            arr.pop()
DFS(0)