# D2 4869. [파이썬 SW 문제해결 기본] 종이붙이기
import math


def square(n):
    cnt = 1
    length1 = n // 10
    length2 = n // 20
    cnt20 = 1
    temp_size = length1
    while temp_size != length2:
        temp_size -= 1
        if temp_size < cnt20:
            break
        combi = (math.factorial(temp_size) // math.factorial(temp_size-cnt20)) // math.factorial(cnt20)
        cnt += combi * (2**cnt20)
        cnt20 += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    size = int(input())
    result = square(size)
    print("#{0} {1}".format(tc, result))