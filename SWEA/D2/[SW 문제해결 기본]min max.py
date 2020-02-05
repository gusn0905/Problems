# D2 min max
T = int(input())
result = []
for v in range(1,T+1):
    length = input()
    nums = input()
    lst = list(map(int,nums.split()))
    for i in range(len(lst)-1,0,-1):
        for j in range(0,i):
            if lst[j] > lst[j+1]:
                lst[j] , lst[j+1] = lst[j+1], lst[j]
    sum = lst[-1] - lst[0]
    result.append(sum)
for v in range(T):
    print("#{0} {1}".format(v+1,result[v]))