# D4 6109 추억의 2048 게임


def spin(lst):
    n = len(lst)
    spin_lst = [[0]*n for _ in range(n)]
    for column in range(n):
        for row in range(n):
            spin_lst[column][row] = lst[n-row-1][column]
    return spin_lst


def game(lst, length):
    unzero_list = []
    for r in range(length):
        tp = []
        for c in range(length):
            if lst[r][c] != 0:
                tp.append(lst[r][c])
        unzero_list.append(tp)
    for r in range(length):
        for c in range(len(unzero_list[r]) - 1):
            if unzero_list[r][c] == 0:
                continue
            elif unzero_list[r][c] == unzero_list[r][c + 1]:
                unzero_list[r][c] *= 2
                unzero_list[r][c + 1] = 0
    final_list = []
    for r in range(length):
        t = []
        for c in range(len(unzero_list[r])):
            if unzero_list[r][c] != 0:
                t.append(unzero_list[r][c])
        final_list.append(t)
    for r in range(length):
        for k in range(length - len(final_list[r])):
            final_list[r].append(0)
    return final_list


def up2048(lst, length):
    lst = spin(lst)
    lst = spin(lst)
    lst = spin(lst)
    result = game(lst, length)
    result = spin(result)
    return result


def down2048(lst, length):
    lst = spin(lst)
    result = game(lst, length)
    result = spin(result)
    result = spin(result)
    result = spin(result)
    return result


def right2048(lst, length):
    lst = spin(lst)
    lst = spin(lst)
    result = game(lst, length)
    result = spin(result)
    result = spin(result)
    return result


def left2048(lst, length):
    result = game(lst, length)
    return result


T = int(input())
for i in range(T):
    temp = list(map(str, input().split()))
    command = ['up', 'down', 'left', 'right']
    size = int(temp[0])
    ctrl = temp[1]
    board = []
    for j in range(size): # 기본 숫자들
        t = list(map(int,input().split()))
        board.append(t)
    if ctrl == command[0]: # up
        board = up2048(board, size)
    elif ctrl == command[1]: # down 맨 아랫라인 고정
        board = down2048(board, size)
    elif ctrl == command[2]: # left 왼쪽 벽라인 고정
        board = left2048(board, size)
    else: # right 오른쪽 벽라인 고정
        board = right2048(board, size)
    print("#{}".format(i+1))
    for r in range(size):
        for c in range(size):
            print(board[r][c], end=' ')
        print()