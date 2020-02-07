# D4 사다리타기
T = 10
for i in range(T):
    num = int(input()) # 테스트 케이스 번호
    ladder = []
    # 사다리 초기화
    for l in range(100):
        temp = list(map(int,input().split()))
        ladder.append(temp)
    r = [0,1,0] # 우 하 좌
    c = [1,0,-1]
    # 답은 시작점의 column 값
    x_list = [] # column들 리스트
    m_list = [] # 이동거리 리스트(거리 중복일때 x가 큰거 찾아야함)
    for column in range(100):
        cnt = 0  # 이동거리
        if ladder[0][column] != 0: # 출발점 지정
            new_x = column
            new_y = 0
            new_y += r[1]
            new_x += c[1]
            while True:
                if new_y >= 99:
                    break
                if new_x == 0:  # 왼쪽 벽일때
                    if ladder[new_y][new_x+1] != 0:  # 오른쪽 사다리로 이동
                        new_y += r[0]
                        new_x += c[0]
                        cnt += 1
                        while ladder[new_y][new_x+1] != 0:  # 오른쪽꺼가 0이 아닐때 까지 이동
                            new_y += r[0]
                            new_x += c[0]
                            cnt += 1
                        # 이동후 다시 돌아오는 무한반복 막기 위해 강제로 한칸 이동
                        # new_y += r[1]
                        # new_x += c[1]
                        # cnt += 1
                elif new_x == 99: # 오른쪽 벽일때
                    if ladder[new_y][new_x - 1] != 0:  # 왼쪽 사다리로 이동
                        new_y += r[2]
                        new_x += c[2]
                        cnt += 1
                        while ladder[new_y][new_x-1] != 0:  # 왼쪽이 0이 아닐때 까지 이동
                            new_y += r[2]
                            new_x += c[2]
                            cnt += 1
                        # 이동후 다시 돌아오는 무한반복 막기 위해 강제로 한칸 이동
                        # new_y += r[1]
                        # new_x += c[1]
                        # cnt += 1
                else:
                    if ladder[new_y][new_x-1] != 0: # 왼쪽 사다리로 이동
                        new_y += r[2]
                        new_x += c[2]
                        cnt += 1
                        while new_x >= 1 and ladder[new_y][new_x-1] != 0:  # 왼쪽이 0이 아닐때 까지 이동
                            new_y += r[2]
                            new_x += c[2]
                            cnt += 1
                        # 이동후 다시 돌아오는 무한반복 막기 위해 강제로 한칸 이동
                        # new_y += r[1]
                        # new_x += c[1]
                        # cnt += 1
                    elif ladder[new_y][new_x+1] != 0: # 오른쪽 사다리로 이동
                        new_y += r[0]
                        new_x += c[0]
                        cnt += 1
                        while new_x <= 98 and ladder[new_y][new_x+1] != 0:  # 오른쪽이 0이 아닐때 까지 이동
                            new_y += r[0]
                            new_x += c[0]
                            cnt += 1
                        # 이동후 다시 돌아오는 무한반복 막기 위해 강제로 한칸 이동
                        # new_y += r[1]
                        # new_x += c[1]
                        # cnt += 1
                new_y += r[1]
                new_x += c[1]
                cnt += 1
            x_list.append(column)
            m_list.append(cnt)

    # 정답 프린트
    minnum = min(m_list)
    idx_list = []
    for j in range(len(m_list)):
        if m_list[j] == minnum:
            idx_list.append(j)
    result = x_list[max(idx_list)]
    #print(x_list)
    #print(m_list)
    print("#{0} {1}".format(num,result))