# D2 4861 [파이썬 S/W 문제해결 기본] 회문


def palindrome(lst, size, length):
    cross_list = []
    result = ''
    for column in range(size):
        temp = []
        for row in range(size):
            temp.append(lst[row][column])
        cross_list.append(temp)
    for row in range(size):
        for column in range(size - length + 1):
            if column == 0:
                if lst[row][column: column + length] == lst[row][column + length - 1:: -1]:
                    result = ''.join(lst[row][column: column + length])
            else:
                if lst[row][column: column + length] == lst[row][column + length - 1:column-1: -1]:
                    result = ''.join(lst[row][column: column + length])
    for row in range(size):
        for column in range(size - length + 1):
            if column == 0:
                if cross_list[row][column: column + length] == cross_list[row][column + length - 1:: -1]:
                    result = ''.join(cross_list[row][column: column + length])
            else:
                if cross_list[row][column: column + length] == cross_list[row][column + length - 1:column-1: -1]:
                    result = ''.join(cross_list[row][column: column + length])
    return result


T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    word_list = []
    for j in range(n):
        tp = input()
        t = list(tp)
        word_list.append(t)
    final = palindrome(word_list, n, m)
    print("#{0} {1}".format(i+1, final))