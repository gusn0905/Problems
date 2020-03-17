# U:w D:y F:r B:o L:g R:b
import copy


def cubing(cmd):
    global cube
    # +는 시계방향, -는 반시계방향으로 90도
    if cmd[0] == 'U':
        if cmd[1] == '-':
            cube[5][6], cube[4][6], cube[3][6], cube[2][5], cube[2][4], cube[2][3], cube[3][2], cube[4][2], cube[5][2], cube[6][3], cube[6][4], cube[6][5] = cube[6][3], cube[6][4], cube[6][5], cube[5][6], cube[4][6], cube[3][6], cube[2][5], cube[2][4], cube[2][3], cube[3][2], cube[4][2], cube[5][2]
            cube[5][5], cube[4][5], cube[3][5], cube[3][5], cube[3][4], cube[3][3], cube[3][3], cube[4][3], cube[5][3], cube[5][3], cube[5][4], cube[5][5] = cube[5][3], cube[5][4], cube[5][5], cube[5][5], cube[4][5], cube[3][5], cube[3][5], cube[3][4], cube[3][3], cube[3][3], cube[4][3], cube[5][3]
        else:
            cube[6][3], cube[6][4], cube[6][5], cube[5][6], cube[4][6], cube[3][6], cube[2][5], cube[2][4], cube[2][3], cube[3][2], cube[4][2], cube[5][2] = cube[5][6], cube[4][6], cube[3][6], cube[2][5], cube[2][4], cube[2][3], cube[3][2], cube[4][2], cube[5][2], cube[6][3], cube[6][4], cube[6][5]
            cube[5][3], cube[5][4], cube[5][5], cube[5][5], cube[4][5], cube[3][5], cube[3][5], cube[3][4], cube[3][3], cube[3][3], cube[4][3], cube[5][3] = cube[5][5], cube[4][5], cube[3][5], cube[3][5], cube[3][4], cube[3][3], cube[3][3], cube[4][3], cube[5][3], cube[5][3], cube[5][4], cube[5][5]
    elif cmd[0] == 'D':
        if cmd[1] == '-':
            cube[3][0], cube[4][0], cube[5][0], cube[0][5], cube[0][4], cube[0][3], cube[5][8], cube[4][8], cube[3][8], cube[8][3], cube[8][4], cube[8][5] = cube[8][3], cube[8][4], cube[8][5], cube[3][0], cube[4][0], cube[5][0], cube[0][5], cube[0][4], cube[0][3], cube[5][8], cube[4][8], cube[3][8]
            cube[11][5], cube[10][5], cube[9][5], cube[9][5], cube[9][4], cube[9][3], cube[9][3], cube[10][3], cube[11][3], cube[11][3], cube[11][4], cube[11][5] = cube[11][3], cube[11][4], cube[11][5], cube[11][5], cube[10][5], cube[9][5], cube[9][5], cube[9][4], cube[9][3], cube[9][3], cube[10][3], cube[11][3]
        else:
            cube[8][3], cube[8][4], cube[8][5], cube[3][0], cube[4][0], cube[5][0], cube[0][5], cube[0][4], cube[0][3], cube[5][8], cube[4][8], cube[3][8] = cube[3][0], cube[4][0], cube[5][0], cube[0][5], cube[0][4], cube[0][3], cube[5][8], cube[4][8], cube[3][8], cube[8][3], cube[8][4], cube[8][5]
            cube[11][3], cube[11][4], cube[11][5], cube[11][5], cube[10][5], cube[9][5], cube[9][5], cube[9][4], cube[9][3], cube[9][3], cube[10][3], cube[11][3] = cube[11][5], cube[10][5], cube[9][5], cube[9][5], cube[9][4], cube[9][3], cube[9][3], cube[10][3], cube[11][3], cube[11][3], cube[11][4], cube[11][5]
    elif cmd[0] == 'L':
        if cmd[1] == '-':
            cube[0][3], cube[1][3], cube[2][3], cube[3][3], cube[4][3], cube[5][3], cube[6][3], cube[7][3], cube[8][3], cube[9][3], cube[10][3], cube[11][3]  = cube[3][3], cube[4][3], cube[5][3], cube[6][3], cube[7][3], cube[8][3], cube[9][3], cube[10][3], cube[11][3], cube[0][3], cube[1][3], cube[2][3]
            cube[5][2], cube[4][2], cube[3][2], cube[5][0], cube[5][1], cube[5][2], cube[3][0], cube[4][0], cube[5][0], cube[3][2], cube[3][1], cube[3][0] = cube[5][0], cube[5][1], cube[5][2], cube[3][0], cube[4][0], cube[5][0], cube[3][2], cube[3][1], cube[3][0], cube[5][2], cube[4][2], cube[3][2]
        else:
            cube[3][3], cube[4][3], cube[5][3], cube[6][3], cube[7][3], cube[8][3], cube[9][3], cube[10][3], cube[11][3], cube[0][3], cube[1][3], cube[2][3] = cube[0][3], cube[1][3], cube[2][3], cube[3][3], cube[4][3], cube[5][3], cube[6][3], cube[7][3], cube[8][3], cube[9][3], cube[10][3], cube[11][3]
            cube[5][0], cube[5][1], cube[5][2], cube[3][0], cube[4][0], cube[5][0], cube[3][2], cube[3][1], cube[3][0], cube[5][2], cube[4][2], cube[3][2] = cube[5][2], cube[4][2], cube[3][2], cube[5][0], cube[5][1], cube[5][2], cube[3][0], cube[4][0], cube[5][0], cube[3][2], cube[3][1], cube[3][0]
    elif cmd[0] == 'R':
        if cmd[1] == '-':
            cube[3][5], cube[4][5], cube[5][5], cube[6][5], cube[7][5], cube[8][5], cube[9][5], cube[10][5], cube[11][5], cube[0][5], cube[1][5], cube[2][5] = cube[0][5], cube[1][5], cube[2][5], cube[3][5], cube[4][5], cube[5][5], cube[6][5], cube[7][5], cube[8][5], cube[9][5], cube[10][5], cube[11][5]
            cube[3][6], cube[3][7], cube[3][8], cube[5][6], cube[4][6], cube[3][6], cube[5][8], cube[5][7], cube[5][6], cube[3][8], cube[4][8], cube[5][8] = cube[3][8], cube[4][8], cube[5][8], cube[3][6], cube[3][7], cube[3][8], cube[5][6], cube[4][6], cube[3][6], cube[5][8], cube[5][7], cube[5][6]
        else:
            cube[0][5], cube[1][5], cube[2][5], cube[3][5], cube[4][5], cube[5][5], cube[6][5], cube[7][5], cube[8][5], cube[9][5], cube[10][5], cube[11][5] = cube[3][5], cube[4][5], cube[5][5], cube[6][5], cube[7][5], cube[8][5], cube[9][5], cube[10][5], cube[11][5], cube[0][5], cube[1][5], cube[2][5]
            cube[3][8], cube[4][8], cube[5][8], cube[3][6], cube[3][7], cube[3][8], cube[5][6], cube[4][6], cube[3][6], cube[5][8], cube[5][7], cube[5][6] = cube[3][6], cube[3][7], cube[3][8], cube[5][6], cube[4][6], cube[3][6], cube[5][8], cube[5][7], cube[5][6], cube[3][8], cube[4][8], cube[5][8]
    elif cmd[0] == 'F':
        if cmd[1] == '-':
            cube[8][5], cube[7][5], cube[6][5], cube[8][3], cube[8][4], cube[8][5], cube[6][3], cube[7][3], cube[8][3], cube[6][5], cube[6][4], cube[6][3] = cube[8][3], cube[8][4], cube[8][5], cube[6][3], cube[7][3], cube[8][3], cube[6][5], cube[6][4], cube[6][3], cube[8][5], cube[7][5], cube[6][5]
            cube[5][0], cube[5][1], cube[5][2], cube[9][5], cube[9][4], cube[9][3], cube[5][6], cube[5][7], cube[5][8], cube[5][3], cube[5][4], cube[5][5] = cube[5][3], cube[5][4], cube[5][5], cube[5][0], cube[5][1], cube[5][2], cube[9][5], cube[9][4], cube[9][3], cube[5][6], cube[5][7], cube[5][8]
        else:
            cube[8][3], cube[8][4], cube[8][5], cube[6][3], cube[7][3], cube[8][3], cube[6][5], cube[6][4], cube[6][3], cube[8][5], cube[7][5], cube[6][5] = cube[8][5], cube[7][5], cube[6][5], cube[8][3], cube[8][4], cube[8][5], cube[6][3], cube[7][3], cube[8][3], cube[6][5], cube[6][4], cube[6][3]
            cube[5][3], cube[5][4], cube[5][5], cube[5][0], cube[5][1], cube[5][2], cube[9][5], cube[9][4], cube[9][3], cube[5][6], cube[5][7], cube[5][8] = cube[5][0], cube[5][1], cube[5][2], cube[9][5], cube[9][4], cube[9][3], cube[5][6], cube[5][7], cube[5][8], cube[5][3], cube[5][4], cube[5][5]
    elif cmd[0] == 'B':
        if cmd[1] == '-':
            cube[3][3], cube[3][4], cube[3][5], cube[3][6], cube[3][7], cube[3][8], cube[11][5], cube[11][4], cube[11][3], cube[3][0], cube[3][1], cube[3][2] = cube[3][0], cube[3][1], cube[3][2], cube[3][3], cube[3][4], cube[3][5], cube[3][6], cube[3][7], cube[3][8], cube[11][5], cube[11][4], cube[11][3]
            cube[2][3], cube[2][4], cube[2][5], cube[2][5], cube[1][5], cube[0][5], cube[0][5], cube[0][4], cube[0][3], cube[0][3], cube[1][3], cube[2][3] = cube[0][3], cube[1][3], cube[2][3], cube[2][3], cube[2][4], cube[2][5], cube[2][5], cube[1][5], cube[0][5], cube[0][5], cube[0][4], cube[0][3]
        else:
            cube[3][0], cube[3][1], cube[3][2], cube[3][3], cube[3][4], cube[3][5], cube[3][6], cube[3][7], cube[3][8], cube[11][5], cube[11][4], cube[11][3] = cube[3][3], cube[3][4], cube[3][5], cube[3][6], cube[3][7], cube[3][8], cube[11][5], cube[11][4], cube[11][3], cube[3][0], cube[3][1], cube[3][2]
            cube[0][3], cube[1][3], cube[2][3], cube[2][3], cube[2][4], cube[2][5], cube[2][5], cube[1][5], cube[0][5], cube[0][5], cube[0][4], cube[0][3] = cube[2][3], cube[2][4], cube[2][5], cube[2][5], cube[1][5], cube[0][5], cube[0][5], cube[0][4], cube[0][3], cube[0][3], cube[1][3], cube[2][3]

    return cube


cube = [['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x'], # 0
        ['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x'], # 1
        ['x', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x'], # 2
        ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'], # 3
        ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'], # 4
        ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'], # 5
        ['x', 'x', 'x', 'r', 'r', 'r', 'x', 'x', 'x'], # 6
        ['x', 'x', 'x', 'r', 'r', 'r', 'x', 'x', 'x'], # 7
        ['x', 'x', 'x', 'r', 'r', 'r', 'x', 'x', 'x'], # 8
        ['x', 'x', 'x', 'y', 'y', 'y', 'x', 'x', 'x'], # 9
        ['x', 'x', 'x', 'y', 'y', 'y', 'x', 'x', 'x'], # 10
        ['x', 'x', 'x', 'y', 'y', 'y', 'x', 'x', 'x']] # 11


T = int(input())
for tc in range(1, T+1):
    init_cube = copy.deepcopy(cube)
    n = int(input())
    order = list(map(str, input().split()))
    for i in range(n):
        cube = cubing(order[i])
    for r in range(3, 6):
        for c in range(3, 6):
            print(cube[r][c], end= '')
        print()
    cube = init_cube  # 초기화


import copy

def rotate(lst, dir):
    new_lst = [[0]*3 for _ in range(3)]
    # 시계방향
    if dir == '+':
        for i in range(3):
            for j in range(3):
                new_lst[i][j] = lst[2-j][i]
        return new_lst

    elif dir == '-':
        for _ in range(3):
            for i in range(3):
                for j in range(3):
                    new_lst[i][j] = lst[2 - j][i]
            lst = copy.deepcopy(new_lst)
        return lst

tc = int(input())
for t in range(1, tc+1):
    n = int(input()) # 돌린횟수
    fd = list(input().split())
    # print(fd)

    # 각각의 면에 대한 2차원 배열 만들기
    u = [['w']*3 for _ in range(3)]
    d = [['y']*3 for _ in range(3)]
    f = [['r']*3 for _ in range(3)]
    b = [['o']*3 for _ in range(3)]
    l = [['g']*3 for _ in range(3)]
    r = [['b']*3 for _ in range(3)]

    for x in fd:
        if x[0] == 'U':
            lst = [b[2][0], b[2][1], b[2][2], r[0][0], r[1][0], r[2][0], f[0][2], f[0][1], f[0][0], l[2][2], l[1][2], l[0][2]]
            if x[1] == '+':
                for i in range(3):
                    b[2][i] = lst[i+9]
                    r[i][0] = lst[i]
                    f[0][2-i] = lst[i+3]
                    l[2-i][2] = lst[i+6]
            else:
                for i in range(3):
                    b[2][i] = lst[i+3]
                    r[i][0] = lst[i+6]
                    f[0][2-i] = lst[i+9]
                    l[2-i][2] = lst[i]
            u = rotate(u, x[1])

        elif x[0] == 'D':
            lst = [f[2][0], f[2][1], f[2][2], r[2][2], r[1][2], r[0][2], b[0][2], b[0][1], b[0][0], l[0][0], l[1][0], l[2][0]]
            if x[1] == '+':
                for i in range(3):
                    f[2][i] = lst[i+9]
                    r[2-i][2] = lst[i]
                    b[0][2-i] = lst[i+3]
                    l[i][0] = lst[i+6]
            else:
                for i in range(3):
                    f[2][i] = lst[i+3]
                    r[2-i][2] = lst[i+6]
                    b[0][2-i] = lst[i+9]
                    l[i][0] = lst[i]
            d = rotate(d, x[1])

        elif x[0] == 'F':
            lst = [u[2][0], u[2][1], u[2][2], r[2][0], r[2][1], r[2][2], d[0][2], d[0][1], d[0][0], l[2][0], l[2][1], l[2][2]]
            if x[1] == '+':
                for i in range(3):
                    u[2][i] = lst[i+9]
                    r[2][i] = lst[i]
                    d[0][2-i] = lst[i+3]
                    l[2][i] = lst[i+6]
            else:
                for i in range(3):
                    u[2][i] = lst[i+3]
                    r[2][i] = lst[i+6]
                    d[0][2-i] = lst[i+9]
                    l[2][i] = lst[i]
            f = rotate(f, x[1])

        elif x[0] == 'B':
            lst = [d[2][0], d[2][1], d[2][2], r[0][2], r[0][1], r[0][0], u[0][2], u[0][1], u[0][0], l[0][2], l[0][1], l[0][0]]
            if x[1] == '+':
                for i in range(3):
                    d[2][i] = lst[i+9]
                    r[0][2-i] = lst[i]
                    u[0][2-i] = lst[i+3]
                    l[0][2-i] = lst[i+6]
            else:
                for i in range(3):
                    d[2][i] = lst[i+3]
                    r[0][2-i] = lst[i+6]
                    u[0][2-i] = lst[i+9]
                    l[0][2-i] = lst[i]
            b = rotate(b, x[1])

        elif x[0] == 'R':
            lst = [b[2][2], b[1][2], b[0][2], d[2][2], d[1][2], d[0][2], f[2][2], f[1][2], f[0][2], u[2][2], u[1][2], u[0][2]]
            if x[1] == '+':
                for i in range(3):
                    b[2-i][2] = lst[i+9]
                    d[2-i][2] = lst[i]
                    f[2-i][2] = lst[i+3]
                    u[2-i][2] = lst[i+6]
            else:
                for i in range(3):
                    b[2-i][2] = lst[i+3]
                    d[2-i][2] = lst[i+6]
                    f[2-i][2] = lst[i+9]
                    u[2-i][2] = lst[i]
            r = rotate(r, x[1])

        elif x[0] == 'L':
            lst = [b[0][0], b[1][0], b[2][0], u[0][0], u[1][0], u[2][0], f[0][0], f[1][0], f[2][0], d[0][0], d[1][0], d[2][0]]
            if x[1] == '+':
                for i in range(3):
                    b[i][0] = lst[i+9]
                    u[i][0] = lst[i]
                    f[i][0] = lst[i+3]
                    d[i][0] = lst[i+6]
            else:
                for i in range(3):
                    b[i][0] = lst[i+3]
                    u[i][0] = lst[i+6]
                    f[i][0] = lst[i+9]
                    d[i][0] = lst[i]
            l = rotate(l, x[1])

    for i in range(3):
        print(''.join(u[i]))