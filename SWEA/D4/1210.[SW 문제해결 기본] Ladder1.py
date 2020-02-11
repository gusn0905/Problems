# D4 1210. [S/W 문제해결 기본] Ladder1
T = 10
for i in range(T):
    num = int(input()) # 테스트 케이스 번호
    ladder = []
    # 사다리 초기화
    for l in range(100):
        temp = list(map(int, input().split()))
        ladder.append(temp)
    start = []
    for l in range(100):
        if ladder[0][l] != 0:
            start.append(l)
    r = [0, 1, 0]  # 우 하 좌
    c = [1, 0, -1]
    # 답은 시작점의 column 값
    result = 0
    for column in start:
        new_r = 0
        new_c = column
        while True:
            if new_c == 0: # 왼쪽 벽
                if ladder[new_r][new_c+1] != 0: # 오른쪽으로 이동
                    new_r += r[0]
                    new_c += c[0]
                    while ladder[new_r][new_c+1] != 0:
                        new_r += r[0]
                        new_c += c[0]
            elif new_c == 99: # 오른쪽 벽
                if ladder[new_r][new_c-1] != 0: # 왼쪽으로 이동
                    new_r += r[2]
                    new_c += c[2]
                    while ladder[new_r][new_c-1] != 0:
                        new_r += r[2]
                        new_c += c[2]
            else:
                if ladder[new_r][new_c-1] != 0: # 왼쪽으로 이동
                    new_r += r[2]
                    new_c += c[2]
                    while new_c >= 1 and ladder[new_r][new_c-1] != 0:
                        new_r += r[2]
                        new_c += c[2]
                elif ladder[new_r][new_c+1] != 0: # 오른쪽으로 이동
                    new_r += r[0]
                    new_c += c[0]
                    while new_c <= 98 and ladder[new_r][new_c+1] != 0:
                        new_r += r[0]
                        new_c += c[0]
            new_r += r[1]
            new_c += c[1]
            if new_r == 99:
                if ladder[new_r][new_c] == 2:
                    result = column
                break
    print("#{0} {1}".format(i+1, result))