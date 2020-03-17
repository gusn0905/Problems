def Horizontal(lst, r, c):
    global result
    global n
    if r == n-1 and c == n-1:
        result += 1
    if c+1 <= n-1 and lst[r][c+1] == 0:
        Horizontal(lst, r, c+1)
        if r+1 <= n-1 and lst[r+1][c] == 0 and lst[r+1][c+1] == 0:
            Diagonal(lst, r+1, c+1)


def Vertical(lst, r, c):
    global result
    global n
    if r == n-1 and c == n-1:
        result += 1
    if r+1 <= n-1 and lst[r+1][c] == 0:
        Vertical(lst, r+1, c)
        if c+1 <= n-1 and lst[r][c+1] == 0 and lst[r+1][c+1] == 0:
            Diagonal(lst, r+1, c+1)


def Diagonal(lst, r, c):
    global result
    global n
    if r == n-1 and c == n-1:
        result += 1
    if c+1 <= n-1 and lst[r][c+1] == 0:
        Horizontal(lst, r, c+1)
    if r+1 <= n-1 and lst[r+1][c] == 0:
        Vertical(lst, r+1, c)
    if c+1 <= n-1 and r+1 <= n-1 and lst[r][c+1] == 0 and lst[r+1][c] == 0 and lst[r+1][c+1] == 0:
        Diagonal(lst, r+1, c+1)


n = int(input())
board = []
for i in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)
result = 0
Horizontal(board, 0, 1)
print(result)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
start = [0, 0]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)] # 좌우, 상하, 대각선
dp[0][1][0] = 1
for i in range(N):
    for j in range(N):
        # if i + 1 >= N or j + 1 >= N:
        #     continue
        if i + 1 < N and j + 1 < N and arr[i + 1][j] != 1 and arr[i][j + 1] != 1 and arr[i + 1][j + 1] != 1:
            dp[i + 1][j + 1][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]
        if j + 1 < N and arr[i][j + 1] != 1:
            dp[i][j + 1][0] += dp[i][j][0] + dp[i][j][2]
        if i + 1 < N and arr[i + 1][j] != 1:
            dp[i + 1][j][1] += dp[i][j][1] + dp[i][j][2]
answer = dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2]
print(answer)