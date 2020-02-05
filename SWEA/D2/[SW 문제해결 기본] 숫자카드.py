# D2 숫자 카드
T = int(input())

# 가장 많이 중복된 개수
maxnum_lst = []
# 가장 많이 나온 수
mostnum_lst = []

for i in range(T):
    card_len = int(input())
    index_lst = [0 for v in range(10)]
    card = input()
    card_list = list(map(int,card))

    # 인덱스 리스트에서 카드 숫자에 해당하는 인덱스의 값 증가
    for num in card_list:
        index_lst[num] += 1

    # 가장 많이 중복된 갯수
    maxnum = max(index_lst)
    maxnum_lst.append(maxnum)

    most_temp = []
    for idx in range(len(index_lst)):
        if index_lst[idx] == maxnum:
            most_temp.append(idx)
    most_temp.sort()
    mostnum = most_temp[-1]
    mostnum_lst.append(mostnum)

for j in range(T):
    print("#{0} {1} {2}".format(j+1,mostnum_lst[j],maxnum_lst[j]))