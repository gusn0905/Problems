# D2 두 개의 숫자열
T = int(input())
for i in range(T):
    n,m = input().split()
    n = int(n)
    m = int(m)
    ai = list(map(int,input().split()))
    bj = list(map(int,input().split()))
    result = []
    if len(ai) < len(bj):
        for j in range(len(bj)-len(ai)+1):
            temp = 0
            for k in range(len(ai)):
                temp += ai[k] * bj[j+k]
            result.append(temp)
    else:
        for j in range(len(ai)-len(bj)+1):
            temp = 0
            for k in range(len(bj)):
                temp += bj[k] * ai[j+k]
            result.append(temp)
    print("#{0} {1}".format(i+1,max(result)))
