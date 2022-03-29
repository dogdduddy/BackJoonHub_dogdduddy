m, n = map(int,input().split())

s = input().split()
s.sort()
arr = [0]*n



def DFS(start, num):
    con = 0
    gat = 0
    temp = ""
    if num == m:
        for i in range(n):
            if arr[i] == 1:
                if s[i] in "aeiou":
                    gat += 1
                    temp += s[i]
                else:
                    con += 1
                    temp += s[i]
        if gat >= 1 and con >= 2:
            print(temp)
        return

    for i in range(start, n):
        arr[i] = 1
        DFS(i+1,num+1)
        arr[i] = 0
DFS(0, 0)