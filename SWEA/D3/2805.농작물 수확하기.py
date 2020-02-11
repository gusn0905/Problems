# D3 2805.농작물 수확하기
def harvest(lst, n):
    idx = n // 2
    total = 0
    for r in range(idx + 1):
        for c in range(idx - r, idx + r + 1):
            total += lst[r][c]
    for r in range(idx + 1, n):
        for c in range(idx - abs(n-r) + 1,idx + abs(n-r)):
            total += lst[r][c]
    return total


T = int(input())
for i in range(T):
    size = int(input())
    farm = []
    for j in range(size):
        tp = input()
        temp = list(tp)
        temp = list(map(int, temp))
        farm.append(temp)
    result = harvest(farm, size)
    print("#{0} {1}".format(i+1, result))