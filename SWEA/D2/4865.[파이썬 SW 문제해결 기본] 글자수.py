# D2 4865 [파이썬 S/W 문제해결 기본] 글자수


# 일반적인 답


def char_count(s1, s2):
    cnt_list = []
    for char in s1:
        cnt_list.append(s2.count(char))
    return max(cnt_list)


T = int(input())
for i in range(T):
    str1 = input()
    str2 = input()
    print("#{0} {1}".format(i+1, char_count(str1, str2)))


# 딕셔너리 이용
def char_count(s1, s2):
    result_dict = {}
    for key in s1:
        result_dict[key] = s2.count(key)
    cnt = []
    for key in result_dict.keys():
        cnt.append(result_dict[key])
    return max(cnt)


T = int(input())
for i in range(T):
    str1 = input()
    str2 = input()
    print("#{0} {1}".format(i+1, char_count(str1, str2)))