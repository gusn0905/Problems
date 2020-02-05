# D3 전기버스

T = int(input())
result = []
for i in range(T):
    basic_inputs = input()
    basic_list = list(map(int,basic_inputs.split()))

    k = basic_list[0] # K
    n = basic_list[1] # N
    m = basic_list[2] # M

    bus_stop = input()
    # 충전기 위치 리스트
    stop_list = list(map(int,bus_stop.split()))
    lc = 0
    sum = 0
    while True:
        lc += k
        if lc >= n:
            break
        if lc in stop_list:
            sum += 1
        else:
            for j in range(m):
                if stop_list[j] > lc:
                    if lc - stop_list[j-1] >= k:
                        sum = 0
                    else:
                        lc = stop_list[j-1]
                        sum += 1
                    break
                elif stop_list[m-1] < lc:
                    sum += 1
                    break
        if sum == 0:
            break
    result.append(sum)

for i in range(T):
    print("#{0} {1}".format(i+1,result[i]))