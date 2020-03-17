def dragon_curve(lst, r, c, d, g):
    dr = [0, -1, 0, 1] # 우 상 좌 하
    dc = [1, 0, -1, 0]
    r_list = []
    c_list = []
    lst[r][c] += 1
    if d == 0:
        r_list.append(0)
        c_list.append(0)
    elif d == 1:
        r_list.append(1)
        c_list.append(1)
    elif d == 2:
        r_list.append(2)
        c_list.append(2)
    else:
        r_list.append(3)
        c_list.append(3)
    # [0], [0, 1], [0, 1, 2, 1], [0, 1, 2, 1, 2, 3, 2, 1]
    while g != 0:
        for i in range(len(r_list)-1, -1, -1):
            r_list.append((r_list[i]+1)%4)
            c_list.append((c_list[i]+1)%4)
        g -= 1
    for i in range(len(r_list)):
        r += dr[r_list[i]]
        c += dc[c_list[i]]
        lst[r][c] += 1

    return lst


# 0: 우, 1: 상, 2: 좌, 3: 하
board = [[0]*101 for _ in range(101)]
N = int(input())
# x,y : 시작점, d: 시작 방향, g: 세대
dragons = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    board = dragon_curve(board, dragons[i][1], dragons[i][0], dragons[i][2], dragons[i][3])

cnt = 0
for r in range(100):
    for c in range(100):
        if board[r][c] != 0 and board[r+1][c] != 0 and board[r][c+1] != 0 and board[r+1][c+1] != 0:
            cnt += 1
print(cnt)