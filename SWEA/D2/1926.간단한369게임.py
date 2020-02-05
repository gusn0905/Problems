# D2 간단한 369게임
T = int(input())
result = [i for i in range(1,T+1)]
for v in range(len(result)):
    cnt = 0
    temp = list(str(result[v]))
    cnt += temp.count('3')
    cnt += temp.count('6')
    cnt += temp.count('9')
    if cnt > 0:
        result[v] = '-' * cnt
for i in range(T):
    print(result[i], end=' ')