# D3 1493. 수의 새로운 연산


def new_operand(a, b):
    temp = []
    for j in range(2,285):
        sum = 0
        for k in range(1,j):
            sum += k
        temp.append(sum)
    x1, y1, x2, y2 = 0, 1, 0, 1
    while True:
        if temp[x1] >= a:
            break
        x1 += 1
    while True:
        if temp[x2] >= b:
            break
        x2 += 1
    len1 = abs(temp[x1] - a)
    len2 = abs(temp[x2] - b)
    x1 -= len1 - 1
    y1 += len1
    x2 -= len2 - 1
    y2 += len2
    x3 = x1 + x2
    y3 = y1 + y2
    new_x = x3 + y3 - 1
    result = temp[new_x-1] - (new_x-x3)
    return result


T = int(input())
for i in range(T):
    num1, num2 = map(int, input().split())
    outcome = new_operand(num1, num2)
    print("#{0} {1}".format(i+1, outcome))