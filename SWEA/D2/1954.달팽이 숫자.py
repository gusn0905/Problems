#D2 달팽이 숫자
T = int(input())
for i in range(T):
    size = int(input())
    snail = [[0] * size for j in range(size)]
    cnt = 1
    dir_list = [1, 2, 3, 4] # 1 = 우 2 = 하 3 = 좌 4 = 상
    dir = 1
    row = 0
    column = 0
    while cnt != (size**2)+1:
        if dir == dir_list[0]:
            if column == size:
                column -= 1
                row += 1
                dir = dir_list[1]
            elif snail[row][column] != 0:
                column -=1
                dir = dir_list[1]
                row += 1
            else:
                snail[row][column] = cnt
                column += 1
                cnt += 1
        elif dir == dir_list[1]:
            if row == size:
                row -= 1
                column -= 1
                dir = dir_list[2]
            elif snail[row][column] != 0:
                row -= 1
                dir = dir_list[2]
                column -= 1
            else:
                snail[row][column] = cnt
                row += 1
                cnt += 1
        elif dir == dir_list[2]:
            if snail[row][column] != 0:
                column += 1
                dir = dir_list[3]
                row -= 1
            else:
                snail[row][column] = cnt
                cnt += 1
                column -= 1
        elif dir == dir_list[3]:
            if snail[row][column] != 0:
                row += 1
                dir = dir_list[0]
                column+=1
            else:
                snail[row][column] = cnt
                cnt += 1
                row -= 1

    print("#{}".format(i+1))
    for row in range(size):
        for column in range(size):
            print(snail[row][column], end=' ')
        print()
