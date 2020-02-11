# D3 1217. [S/W 문제해결 기본] 거듭 제곱
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)


T = 10
for i in range(T):
    num = int(input())
    num1, num2 = map(int, input().split())
    result = power(num1, num2)
    print("#{0} {1}".format(num, result))