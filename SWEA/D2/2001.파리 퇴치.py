# D2 파리 퇴치
T = int(input())
result = []
for i in range(T):
    n, m = input().split()
    n = int(n)
    m = int(m)
    fly_list = []
    sum_list = []
    for f in range(n):
        fly = input()
        temp = list(map(int,fly.split()))
        fly_list.append(temp)
    for row in range(n-m+1):
        for column in range(n-m+1):
            sum = 0
            for a in range(row,row+m):
                for b in range(column,column+m):
                    sum += fly_list[a][b]
            sum_list.append(sum)
    print("#{0} {1}".format(i+1,max(sum_list)))