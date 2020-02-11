# D3 1234. [S/W 문제해결 기본] 비밀번호
def password(lst):
    idx = 0
    while idx != len(lst):
        if idx == len(lst) - 1:
            break
        if lst[idx] == lst[idx + 1]:
            del lst[idx: idx + 2]
            idx = 0
        else:
            idx += 1
    return lst


T = 10
for i in range(T):
    base = list(map(str, input().split()))
    size = int(base[0])
    num_list = list(base[1])
    num_list = password(num_list)
    print("#{}".format(i+1), end=' ')
    for j in range(len(num_list)):
        print(num_list[j], end='')
    print()