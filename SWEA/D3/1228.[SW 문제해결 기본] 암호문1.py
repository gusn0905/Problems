# D3 1228. [S/W 문제해결 기본] 암호문1
def encryption(org_lst, lst):
    idx2 = lst[1]
    length2 = lst[2]
    for k in range(3, 3 + length2):
        if idx2 >= len(org_lst):
            continue
        else:
            org_lst.insert(idx2,lst[k])
            idx2 += 1
    return org_lst


T = 10
for i in range(T):
    size = int(input())
    original = list(map(int, input().split()))
    length = int(input())
    temp = list(map(str, input().split()))
    encrypt = []
    idx = -1
    for j in temp:
        if j == 'I':
            encrypt.append([j])
            idx += 1
        else:
            encrypt[idx].append(j)
    for r in range(length):
        for c in range(1, 2 + int(encrypt[r][2]) + 1):
            encrypt[r][c] = int(encrypt[r][c])
    for j in range(length):
        original = encryption(original, encrypt[j])
    print("#{}".format(i+1), end=' ')
    for j in range(10):
        print(original[j], end=' ')
    print()