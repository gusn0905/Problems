# D2 1974. 스도쿠 검증

T = int(input())
result_list = []
for i in range(T):
    sudoku = []
    cnt = 0
    for j in range(9):
        temp = list(map(int,input().split()))
        sudoku.append(temp)
    for j in range(9):
        temp_set = set(sudoku[j])
        #print(temp_set)
        if len(temp_set) != 9:
            cnt += 1
    for c in range(9):
        temp = []
        for r in range(9):
            temp.append(sudoku[r][c])
        temp_set = set(temp)
        if len(temp_set) != 9:
            cnt += 1
    for r in range(0,7,3):
        for c in range(0,7,3):
            temp = []
            for j in range(r,r+3):
                for k in range(c,c+3):
                    temp.append(sudoku[j][k])
            temp_set = set(temp)
            #print(temp_set)
            if len(temp_set) != 9:
                cnt += 1
    if cnt == 0:
        result = 1
    else:
        result = 0
    result_list.append(result)

for i in range(T):
    print("#{0} {1}".format(i+1,result_list[i]))