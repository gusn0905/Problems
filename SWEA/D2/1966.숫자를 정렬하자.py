# D2 1966. 숫자를 정렬하자


T = int(input())
for i in range(T):
    size = int(input())
    lst = list(map(int,input().split()))
    print(lst)
    for j in range(size-1,0,-1):
        for k in range(j):
            if lst[k] > lst[k+1]:
                lst[k], lst[k+1] = lst[k+1], lst[k]
    print("{0}".format(i+1),end=' ')
    for j in range(size):
        print(lst[j], end=' ')
    print()