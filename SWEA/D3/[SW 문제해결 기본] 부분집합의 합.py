# [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
T = int(input())
for i in range(T):
    n,k = input().split()
    n = int(n)
    k = int(k)
    arr = [j for j in range(1,13)]
    subset = []
    for j in range(1,1<<12):
        temp = []
        for v in range(12):
            if j & (1<<v):
                temp.append(arr[v])
        subset.append(temp)
    cnt = 0
    for j in range(len(subset)):
        if len(subset[j]) == n and sum(subset[j]) == k:
            cnt += 1
    print("#{0} {1}".format(i+1,cnt))