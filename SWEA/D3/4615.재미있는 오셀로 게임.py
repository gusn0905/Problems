# D3 4615. 재미있는 오셀로 게임
T = int(input())
for i in range(T):
    # 보드 초기화
    N,M = map(int,input().split())
    board = [[0] * N for j in range(N)]
    idx = N // 2
    board[idx][idx],board[idx][idx-1],board[idx-1][idx],board[idx-1][idx-1] = 2,1,1,2
    order = []
    for j in range(M):
        temp = list(map(int,input().split()))
        temp[0] = temp[0]-1
        temp[1] = temp[1]-1
        order.append(temp)
    ro = [0,1,0,-1,-1,1,1,-1] # 우 하 좌 상 우상 우하 좌하 좌상
    co = [1,0,-1,0,1,1,-1,-1]
    for j in range(M):
        board[order[j][1]][order[j][0]] = order[j][2]
        column = order[j][0]
        row = order[j][1]
        c = order[j][2]
        for k in range(8):
            new_r = row + ro[k] # 출발
            new_c = column + co[k]
            flag = 0
            temp = []
            while 0 <= new_r <= N-1 and 0 <= new_c <= N-1:
                if board[new_r][new_c] == 0:
                    break
                if board[new_r][new_c] != c:
                    temp.append([new_r,new_c])
                    new_r += ro[k]
                    new_c += co[k]
                    #print(temp)
                    #continue
                elif board[new_r][new_c] == c:
                    flag = 1
                    break


            if flag == 1:
                for r in range(len(temp)):
                    if c == 1:
                        board[temp[r][0]][temp[r][1]] = 1
                    else:
                        board[temp[r][0]][temp[r][1]] = 2
        #print(board)
    cnt1 = 0
    cnt2 = 0
    for j in range(N):
        for k in range(N):
            if board[j][k] == 1:
                cnt1 += 1
            elif board[j][k] == 2:
                cnt2 += 1
    print("#{0} {1} {2}".format(i+1,cnt1,cnt2))