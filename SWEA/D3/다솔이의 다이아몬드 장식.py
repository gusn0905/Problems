# D3 다솔이의 다이아몬드 장식
T = int(input())
for i in range(T):
    word = input()
    column = 1 + 4*len(word)
    row = 5
    showcase = [['.'] * column for j in range(row)]
    for r in range(row):
        cnt = 0
        for c in range(column):
            if r == 2:
                showcase[r][0] = '#'
                if (c-1) % 4 == 1:
                    showcase[r][c] = word[cnt]
                    cnt+=1
                elif (c-1) %4 == 3:
                    showcase[r][c] = '#'
            elif r == 0 or r==4:
                showcase[r][2],showcase[r][column-3] = '#','#'
                if (c -2) % 4 == 0:
                    showcase[r][c] = '#'
            else:
                if c % 2:
                    showcase[r][c] = '#'
    for r in range(row):
        for c in range(column):
            print(showcase[r][c],end='')
        print()