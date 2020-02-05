# D2 1970. 쉬운 거스름돈

def exchange(num):
    tenT = num // 10000
    num -= tenT * 10000
    tou = num // 1000
    num -= tou * 1000
    hun = num // 100
    num -= hun * 100
    ten = num // 10
    lst = [tenT,tou,hun,ten]
    return lst

T = int(input())
for i in range(T):
    num = int(input())
    currency = [0] * 8
    lst = exchange(num)
    for j in range(8):
        if j % 2:
            currency[j] = lst[j//2] % 5
        else:
            currency[j] = lst[j//2] // 5
    print("#{}".format(i+1))
    for j in range(len(currency)):
        print(currency[j],end=' ')
    print()