#[S/W 문제해결 응용]7일차 - 금속막대
T = int(input())
for i in range(T):
    num = int(input())
    temp = list(map(int, input().split()))
    bolts = []
    for j in range(0,len(temp),2):
        bolt = [temp[j],temp[j+1]]
        bolts.append(bolt)
    result = []
    for j in range(num):
        temp = []
        temp.append(bolts[j])
        idx = 0
        cnt = 0
        while cnt != num:
            for k in range(num):
                if temp[idx][1] == bolts[k][0]:
                    temp.append(bolts[k])
                    idx += 1
            else:
                cnt += 1
        result.append(temp)
    ix = 0
    for j in range(1,len(result)):
        if len(result[ix]) <= len(result[j]):
            ix = j
    outcome = result[ix]
    final = []
    for row in range(len(outcome)):
        for column in range(len(outcome[row])):
            final.append(outcome[row][column])
    print("#{}".format(i+1),end =' ')
    for j in range(len(final)):
        print(final[j], end=' ')
    print()