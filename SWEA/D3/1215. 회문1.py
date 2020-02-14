# D3 1215. 회문1
def palindrome(lst, n):
    column_list = []
    cnt = 0
    result_list = []
    for c in range(8):
        temp = []
        for r in range(8):
            temp.append(lst[r][c])
        column_list.append(temp)
    for j in range(8):
        for k in range(8-n+1):
            if k == 0:
                if lst[j][k:k + n] == lst[j][k + n - 1::-1]:
                    result = ''.join(lst[j][k:k+n])
                    result_list.append(result)
                    cnt += 1
            else:
                if lst[j][k:k + n] == lst[j][k + n - 1:k - 1:-1]:
                    result = ''.join(lst[j][k:k + n])
                    result_list.append(result)
                    cnt += 1
    for j in range(8):
        for k in range(8-n+1):
            if k == 0:
                if column_list[j][k:k+n] == column_list[j][k+n-1::-1]:
                    result = ''.join(column_list[j][k:k + n])
                    result_list.append(result)
                    cnt += 1
            else:
                if column_list[j][k:k+n] == column_list[j][k+n-1:k-1:-1]:
                    result = ''.join(column_list[j][k:k + n])
                    result_list.append(result)
                    cnt += 1
    return cnt


T = 10
for i in range(T):
    size = int(input())
    word_list = []
    for j in range(8):
        word = input()
        temp = list(word)
        word_list.append(temp)
    result = palindrome(word_list, size)
    print("#{0} {1}".format(i+1, result))