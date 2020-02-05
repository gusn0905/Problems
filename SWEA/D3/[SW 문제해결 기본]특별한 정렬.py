# [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬
T = int(input())
for i in range(T):
    num = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    result = []
    for j in range(num):
        if j % 2 == 0:
            result.append(max(lst[:num -(j//2)]))
        else:
            result.append(min(lst[j//2:]))
    print("#{}".format(i+1), end=' ')
    for v in range(10):
        print(result[v],end = ' ')
    print()