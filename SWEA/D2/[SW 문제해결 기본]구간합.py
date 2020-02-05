# D2 구간합
T = int(input())
result = []
for i in range(T):
    base = input()
    basic_list = list(map(int,base.split()))
    n = basic_list[0]
    m = basic_list[1]
    nums = input()
    numbers = list(map(int,nums.split()))
    sum_list = []
    for v in range(n-m+1):
        sum = 0
        for k in range(v,v+m):
            sum += numbers[k]
        sum_list.append(sum)
    sum_list.sort()
    result.append(sum_list[-1] - sum_list[0])

for j in range(T):
    print("#{0} {1}".format(j+1, result[j]))