# D2 Base 64 Decoder
ex1 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
base_dict = {}
for i in range(63):
    base_dict[ex1[i]] = i
T = int(input())
result = []
for i in range(T):
    words = input()
    temp = []
    for word in words:
        temp.append(bin(base_dict[word]))
    for bi in range(len(temp)):
        temp[bi] = str(temp[bi])
        temp[bi] = temp[bi][2:]
    for bi in range(len(temp)):
        if len(temp[bi]) < 6:
            temp[bi] = '0' * (6-len(temp[bi])) + temp[bi]
    bin_list = ['' for i in range((len(temp)//4))]
    cnt = 0
    for bi in range(len(temp)):
        bin_list[cnt//4] += temp[bi]
        cnt += 1
    final_list = []
    for bi in range(len(bin_list)):
        final_list.append(bin_list[bi][0:8])
        final_list.append(bin_list[bi][8:16])
        final_list.append(bin_list[bi][16:24])
    for bi in range(len(final_list)):
        final_list[bi] = '0b' + final_list[bi]
    final = ''
    for bi in final_list:
        final += chr(int(bi,2))
    result.append(final)

for i in range(T):
    print("#{0} {1}".format(i+1, result[i]))