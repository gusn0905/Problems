# D3 1220. [S/W 문제해결 기본] Magnetic
def magnetic(lst, n):
    cnt = 0
    new_lst = []
    for row in range(n):
        temp = []
        for column in range(n):
            if lst[row][column] != 0:
                temp.append(lst[row][column])
        new_lst.append(temp)
    for row in range(n):
        for column in range(len(new_lst[row]) - 1):
            if new_lst[row][column] == 1 and new_lst[row][column + 1] == 2:
                cnt += 1
    return cnt


T = 10
for i in range(T):
    size = int(input())
    # N극이 1 S극이 2
    temp = []
    for j in range(100):
        t = list(map(int, input().split()))
        temp.append(t)
    magnet = []
    for column in range(100):
        tp = []
        for row in range(100):
            tp.append(temp[row][column])
        magnet.append(tp)
    result = magnetic(magnet, size)
    print("#{0} {1}".format(i+1, result))