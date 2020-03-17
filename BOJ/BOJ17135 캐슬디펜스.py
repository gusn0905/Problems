# BOJ 17135 캐슬디펜스
import copy
def push(lst):
    empty = [0 for _ in range(M)]
    del lst[-2]
    lst.insert(0, empty)
    return lst


def end(lst):
    l = len(lst)
    s = 0
    for le in range(l-1):
        s += sum(lst[le])
    if s == 0:
        return True
    else:
        return False


def archer(m):
    lst = []
    for a1 in range(m-2):
        for a2 in range(a1+1, m-1):
            for a3 in range(a2+1, m):
                lst.append([a1, a2, a3])
    return lst


N, M, D = map(int, input().split())
board = []
for i in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)
board.append([-1 for _ in range(M)])
arc = archer(M)  # [0, 1, 2] [ 0, 1, 3]
result = []
# 빈칸 0 적 1 궁수 숫자
while len(arc) != 0: # [[0,1,2],[0,1,3],....]
    init_board = copy.deepcopy(board)  # while 문에서 초기화 용
    cnt = 0
    a = arc.pop() # [2,3,4]
    while not end(board): # 게임판에 1이 없을떄까지
        t = [[] for _ in range(N)]
        for ar in a:
            board[-1][ar] = ar
        idx = 0
        while idx != 3:
            minR = 100 # 최소 r
            minD = D # 최소 거리
            minC = 100 # 최소 c
            for r in range(N-1, -1, -1):
                if abs(r - N) > D: # D = 1  r = 2 N = 4
                    break
                for c in range(M):
                    if board[r][c] == 1: # a = [2, 3, 4]
                        dis = abs(r - N) + abs(c - a[idx]) # idx = 0
                        if dis < minD:
                            minD = dis
                            minC = c
                            minR = r
                        elif dis == minD:
                            if c < minC:
                                minR = r
                                minC = c
            if minC < M:
                t[minR].append(minC)
            idx += 1
        for r in range(N):
            cnt += len(set(t[r]))
            for k in t[r]:
                board[r][k] = 0
        board = push(board)
    board = init_board
    result.append(cnt)
print(max(result))



