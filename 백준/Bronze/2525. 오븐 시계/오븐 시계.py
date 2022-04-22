h, m = map(int, input().split())
cook = int(input())
print((h + cook//60 + (m + cook%60)//60)%24,(m + cook%60)%60)
