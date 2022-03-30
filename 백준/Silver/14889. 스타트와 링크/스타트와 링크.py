import sys

n = int(sys.stdin.readline())

people = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
teamA = []

cnt = 0

answer = 1980

def DFS(start, cnt) :
    global answer

    if cnt == n//2:
        cntA = 0
        cntB = 0
        teamB = []
        for i in range(n):
            if i not in teamA:
                teamB.append(i)

        for i in range(n//2):
            for j in range(n//2):
                cntA += people[teamA[j]][teamA[i]]
                cntB += people[teamB[j]][teamB[i]]
        answer = min(answer, abs(cntA-cntB))
        return

    for i in range(start, n):
        if i not in teamA:
            teamA.append(i)
            DFS(i+1, cnt+1)
            teamA.remove(i)
DFS(0, 0)
print(answer)
