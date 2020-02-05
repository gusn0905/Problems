# D2 1976. 시각 덧셈
T = int(input())
for i in range(T):
    times = list(map(int,input().split()))
    time,minute = 0,0
    if (times[0] + times[2]) == 12:
        time = 12
    else:
        time = (times[0] + times[2]) % 12
    if (times[1] + times[3]) >= 60:
        time += 1
        minute = (times[1] + times[3]) % 60
    else:
        minute = (times[1] + times[3]) % 60
    print("#{0} {1} {2}".format(i+1,time,minute))