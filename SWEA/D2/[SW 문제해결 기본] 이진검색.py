# [파이썬 S/W 문제해결 기본] 2일차 - 이진검색
def binarySearch(end,key):
    start = 1
    cnt = 0
    while abs(start-end) != 1:
        middle = int((start + end) / 2)
        if middle == key:
            cnt += 1
            return cnt # 검색 성공
        elif middle > key:
            cnt += 1
            end = middle
        else:
            start = middle
            cnt += 1
    return False # 검색 실패
T = int(input())
for i in range(T):
    temp = list(map(int,input().split()))
    far= temp[0]
    pa = temp[1]
    pb = temp[2]
    cnt1 = binarySearch(far,pa)
    cnt2= binarySearch(far,pb)
    result = ''
    if cnt1 > cnt2:
        result = 'B'
    elif cnt1 == cnt2:
        result = 0
    else:
        result = 'A'
    print("#{0} {1}".format(i+1,result))