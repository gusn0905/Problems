# D3 1213. [S/W 문제해결 기본] String
T = 10
for i in range(T):
    num = int(input())
    search = input()
    words = input()
    result = words.count(search)
    print("#{0} {1}".format(num,result))