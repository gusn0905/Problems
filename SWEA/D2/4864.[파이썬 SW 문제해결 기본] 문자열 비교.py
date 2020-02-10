# D2 4864 [파이썬 S/W 문제해결 기본] 문자열 비교


# def str_check(w1, w2):
#     if w1 in w2:
#         return 1
#     else:
#         return 0


def str_check(w1, w2):
    m = len(w1)
    n = len(w2)
    i = 0
    j = 0
    while j < m and i < n:
        if w2[i] != w1[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == m:
        return 1
    else:
        return 0


T = int(input())
for i in range(T):
    word1 = input()
    word2 = input()
    result = str_check(word1, word2)
    print("#{0} {1}".format(i+1, result))