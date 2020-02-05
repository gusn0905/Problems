# D2  1979.어디에 단어가 들어갈 수 있을까


def isAvailable(lst,k):
    cnt = 0
    for h in range(len(lst)-k+1):
        if sum(lst[h:h+k]) == k:
            if h+k == len(lst) and lst[h-1] != 1:
                cnt += 1
            elif h == 0:
                if lst[h+k] == 0:
                    cnt += 1
            else:
                if lst[h-1]!= 1 and lst[h+k] !=1:
                    cnt += 1
    return cnt


T = int(input())
for i in range(T):
    n,k = map(int,input().split())
    cross_row = []
    cross_column = []
    for _ in range(n):
        temp= []
        temp = list(map(int,input().split()))
        cross_row.append(temp)
    for r in range(n):
        temp = []
        for c in range(n):
            temp.append(cross_row[c][r])
        cross_column.append(temp)
    cnt = 0
    for row in range(n):
        cnt += isAvailable(cross_row[row],k)
    for column in range(n):
        cnt += isAvailable(cross_column[column],k)
    print("#{0} {1}".format(i+1,cnt))