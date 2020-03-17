# BOJ 17144 미세먼지 안녕!
def spreadU(lst, row1, c):
    # lst: board, row1 = cleaner[0], r: row, c: column
    tp1 = [0 for _ in range(c)]
    tp2 = [0 for _ in range(row1)]
    tp3 = [0 for _ in range(c-1)]
    tp4 = [0 for _ in range(row1 - 1)]
    tp1[0] = -1
    for co in range(1, c-1):
        tp1[co+1] = lst[row1][co]
    for ro in range(row1):
        tp2[ro] = lst[row1-ro][c-1]
    for co in range(c-1, 0, -1):
        tp3[co-1] = lst[0][co]
    for ro in range(row1 - 1):
        tp4[ro] = lst[ro][0]

    lst[row1] = tp1
    for ro in range(row1):
        lst[row1-ro-1][c-1] = tp2[ro]
    for co in range(c-1):
        lst[0][co] = tp3[co]
    for ro in range(row1-1):
        lst[ro+1][0] = tp4[ro]

    return lst

def spreadD(lst, row2, r, c):
    # lst: board, row2 = cleaner[0], r: row, c: column
    tp1 = [0 for _ in range(c)]
    tp2 = [0 for _ in range(r - row2)]
    tp3 = [0 for _ in range(c-1)]
    tp4 = [0 for _ in range(r - row2 - 1)]
    tp1[0] = -1
    for co in range(1, c-1):
        tp1[co+1] = lst[row2][co]
    for ro in range(row2, r-1):
        tp2[ro- row2] = lst[ro][c-1]
    for co in range(c-1):
        tp3[co] = lst[r-1][co+1]
    for ro in range(r-1, row2, -1):
        tp4[r-1-ro] = lst[ro][0]

    lst[row2] = tp1
    for ro in range(row2+1, r):
        lst[ro][c-1] = tp2[ro - row2 - 1]
    for co in range(c-1):
        lst[r-1][co] = tp3[co]
    for ro in range(r-2, row2, -1):
        lst[ro][0] = tp4[r-2-ro]

    return lst


row, column, time = map(int,input().split())
board = []
for r in range(row):
    temp = list(map(int, input().split()))
    board.append(temp)
cleaner = []
for r in range(row):
    for c in range(column):
        if board[r][c] == -1:
            cleaner.append(r)
temp = [[0] * column for _ in range(row)]
t1 = time
t2 = time
while t1 != 0:
    for r in range(row):
        for c in range(column):
            cnt = 0
            div = board[r][c] // 5
            if board[r][c] != 0 and board[r][c] != -1:
                if c != 0 and board[r][c-1] != -1: # 왼쪽
                    temp[r][c-1] += div
                    cnt += 1
                if c+1 != column: # 오른쪽
                    temp[r][c+1] += div
                    cnt += 1
                if r != 0 and board[r-1][c] != -1:
                    temp[r-1][c] += div
                    cnt += 1
                if r+1 != row and board[r+1][c] != -1:
                    temp[r+1][c] += div
                    cnt += 1
            board[r][c] -= div * cnt
    for r in range(row):
        for c in range(column):
            board[r][c] += temp[r][c]
    temp = [[0] * column for _ in range(row)]
    board = spreadU(board, cleaner[0], column)
    board = spreadD(board, cleaner[1], row, column)
    t1 -= 1
result = 0
for r in range(row):
    for c in range(column):
        if board[r][c] != -1:
            result += board[r][c]
print(result)

