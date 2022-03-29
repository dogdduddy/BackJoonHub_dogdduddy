n, m = map(int,input().split())
least = 50*50//2

wb = {"W":0, "B":1}
board = [[0 for _ in range(m)]for _ in range(n)]

paint_w = 0
paint_b = 1
for i in range(n):
    board[i][:] = list(input())


for i in range(n-7):
    for j in range(m-7):
        w_cnt = 0
        b_cnt = 0
        for k in range(8):
            for q in range(8):
                if wb[board[i+k][j+q]] != paint_w:
                    w_cnt += 1
                if wb[board[i+k][j+q]] != paint_b:
                    b_cnt += 1
                paint_w, paint_b = paint_b, paint_w
            paint_w, paint_b = paint_b, paint_w
        least = min(least,min(w_cnt,b_cnt))
print(least)