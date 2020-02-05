# [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
T = int(input())
for i in range(T):
    basic_list = [[0]* 100 for i in range(100)]
    nums = int(input())
    colors = []
    for j in range(nums):
        temp = list(map(int,input().split()))
        colors.append(temp)
    for j in range(nums):
        for row in range(colors[j][0],colors[j][2]+1):
            for column in range(colors[j][1],colors[j][3]+1):
                basic_list[row][column] += 1
    cnt = 0
    for row in range(100):
        for column in range(100):
            if basic_list[row][column] > 1:
                cnt += 1
    print("#{0} {1}".format(i+1,cnt))