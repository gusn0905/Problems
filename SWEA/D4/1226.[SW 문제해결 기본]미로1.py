# D4 1226.[S/W 문제해결 기본] 미로1
def find_next(lst, visit, row, column):
    # lst: 미로, visit: visited, row: vr, column = vc
    dr = [0, 1, 0, -1]  # 우 하 좌 상
    dc = [1, 0, -1, 0]
    st = []
    for i in range(4):
        if lst[row + dr[i]][column + dc[i]] == 0 and visit[row + dr[i]][column + dc[i]] == 0 or lst[row + dr[i]][column + dc[i]] == 3:
            st.append([row + dr[i], column + dc[i]])
    return st


def dfs(lst, start_row, start_column):
    # lst: 미로 판, start_row: 시작 row, start_column: 시작 column
    visited = [[0] * 16 for _ in range(16)]
    # find = 0
    stack = []
    stack.append([start_row, start_column])
    while len(stack) > 0:
        v = stack.pop(-1)  # (7,7)
        vr, vc = v[0], v[1]
        visited[vr][vc] = 1
        temp = find_next(lst, visited, vr, vc)
        stack += temp
        if len(stack) == 0:
            break
        wr, wc = stack[-1][0], stack[-1][1]
        #stack.append([wr, wc])
        if lst[wr][wc] == 3:
            return 1
    return 0


T = 10
for tc in range(1, T+1):
    num = int(input())
    maze = []
    for j in range(16):
        t = input()
        temp = list(t)
        temp = list(map(int, temp))
        maze.append(temp)
    v = []
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                v = [r, c]
    result = dfs(maze, v[0], v[1])
    print("#{0} {1}".format(tc, result))