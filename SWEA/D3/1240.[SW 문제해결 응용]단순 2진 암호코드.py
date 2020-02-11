# D3 1240.[S/W 문제해결 응용] 단순 2진 암호코드
def check(lst):
    digit = 0
    if lst == [0,0,0,1,1,0,1]:
        digit = 0
    elif lst == [0,0,1,1,0,0,1]:
        digit = 1
    elif lst == [0,0,1,0,0,1,1]:
        digit = 2
    elif lst == [0,1,1,1,1,0,1]:
        digit = 3
    elif lst == [0,1,0,0,0,1,1]:
        digit = 4
    elif lst == [0,1,1,0,0,0,1]:
        digit = 5
    elif lst == [0,1,0,1,1,1,1]:
        digit = 6
    elif lst == [0,1,1,1,0,1,1]:
        digit = 7
    elif lst == [0,1,1,0,1,1,1]:
        digit = 8
    elif lst == [0,0,0,1,0,1,1]:
        digit = 9
    return digit


def password_check(lst):
    sum = 0
    for p in range(7):
        if p % 2 == 0:
            sum += lst[p] * 3
        else:
            sum += lst[p]
    sum += lst[7]
    return sum


T = int(input())
for i in range(T):
    row, column = map(int, input().split())
    digits = []
    for j in range(row):
        tp = input()
        temp = list(tp)
        digits.append(temp)
    idx1 = 0
    for r in range(row):
        for c in range(column):
            if digits[r][c] != '0':
                idx1 = r
        if idx1 != 0:
            break
    digits[idx1] = list(map(int, digits[idx1]))
    idx2 = 0
    for c in range(column):
        if digits[idx1][c] != 0:
            idx2 = c
    check_digit = digits[idx1][idx2-55:idx2+1]
    final = []
    for k in range(0, 56, 7):
        t = check_digit[k:k+7]
        final.append(t)
    result = []
    for k in range(8):
        result.append(check(final[k]))
    check_num = password_check(result)
    res = 0
    if check_num % 10 == 0:
        res = sum(result)
    else:
        res = 0
    print("#{0} {1}".format(i+1, res))