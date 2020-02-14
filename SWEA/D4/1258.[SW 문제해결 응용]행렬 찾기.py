# D4 1258. [S/W 문제해결 응용] 행렬찾기
def find_rc(lst, n, rc_list):
    new_r = 0
    new_c = 0
    while lst[new_r][new_c] == 0:
        new_c += 1
        if new_c == n - 1:
            new_c = 0
            new_r += 1
        if new_r == n - 1:
            break
    if new_r == n - 1:
        return rc_list
    c1 = new_c
    r1 = new_r
    c2 = 0
    r2 = 0
    for c in range(c1, n):
        if lst[new_r][c] == 0:
            c2 = c
            break
        elif c == n - 1:
            c2 = c + 1
            break
    for r in range(r1, n):
        if lst[r][new_c] == 0:
            r2 = r
            break
        elif r == n-1:
            r2 = r + 1
            break
    r3 = r2 - r1
    c3 = c2 - c1
    rc_list.append([r3, c3])
    for r in range(r1, r2):
        for c in range(c1, c2):
            lst[r][c] = 0
    return find_rc(lst, n, rc_list)


def new_sort(lst):
    mul_list = []
    for k in range(len(lst)):
        mul_list.append(lst[k][0] * lst[k][1])
    mul_list.sort()
    s = [0 for _ in range(len(lst))]
    for k in range(len(lst)):
        if s[mul_list.index(lst[k][0] * lst[k][1])] == 0:
            s[mul_list.index(lst[k][0] * lst[k][1])] = lst[k]
        else:
            s[mul_list.index(lst[k][0] * lst[k][1]) + 1] = lst[k]
    for k in range(len(s) - 1):
        if s[k][0] * s[k][1] == s[k+1][0] * s[k+1][1] and s[k][0] > s[k+1][0]:
            s[k], s[k+1] = s[k+1], s[k]
    return s


T = int(input())
for i in range(T):
    size = int(input())
    matrix = []
    for j in range(size):
        temp = list(map(int, input().split()))
        matrix.append(temp)
    result_list = []
    result = find_rc(matrix, size, result_list)
    cnt = len(result)
    final = new_sort(result)
    print("#{0} {1}".format(i+1, cnt), end=' ')
    for r in range(len(final)):
        for c in range(2):
            print(final[r][c], end=' ')
    print()