# D3 1216. 회문2
def palindrome(lst, column_list, n):
    result_list = []
    for j in range(100):
        for k in range(100-n+1):
            if k == 0:
                if lst[j][k:k + n] == lst[j][k + n - 1::-1]:
                    result = ''.join(lst[j][k:k+n])
                    result_list.append(result)
            else:
                if lst[j][k:k + n] == lst[j][k + n - 1:k-1:-1]:
                    result = ''.join(lst[j][k:k + n])
                    result_list.append(result)
    for j in range(100):
        for k in range(100-n+1):
            if k == 0:
                if column_list[j][k:k+n] == column_list[j][k+n-1::-1]:
                    result = ''.join(column_list[j][k:k + n])
                    result_list.append(result)
            else:
                if column_list[j][k:k+n] == column_list[j][k+n-1:k-1:-1]:
                    result = ''.join(column_list[j][k:k + n])
                    result_list.append(result)
    return result_list


T = 10
for i in range(T):
    num = int(input())
    word_list = []
    for j in range(100):
        word = input()
        temp = list(word)
        word_list.append(temp)
    c_word_list = []
    for c in range(100):
        temp = []
        for r in range(100):
            temp.append(word_list[r][c])
        c_word_list.append(temp)
    temp = []
    for j in range(1, 101):
        temp.append(palindrome(word_list, c_word_list, j))
    result = 0
    for r in range(100):
        if len(temp[r]) > 0:
            result = r+1
    print("#{0} {1}".format(i+1, result))