# D3 1221. GNS


def new_counting_sort(u_lst, s_lst):
    num_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    for n in u_lst:
        if n == 'ZRO':
            num_dict['ZRO'] += 1
        elif n == 'ONE':
            num_dict['ONE'] += 1
        elif n == 'TWO':
            num_dict['TWO'] += 1
        elif n == 'THR':
            num_dict['THR'] += 1
        elif n == 'FOR':
            num_dict['FOR'] += 1
        elif n == 'FIV':
            num_dict['FIV'] += 1
        elif n == 'SIX':
            num_dict['SIX'] += 1
        elif n == 'SVN':
            num_dict['SVN'] += 1
        elif n == 'EGT':
            num_dict['EGT'] += 1
        elif n == 'NIN':
            num_dict['NIN'] += 1
    key_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for j in range(1, len(key_lst)):
        num_dict[key_lst[j]] += num_dict[key_lst[j-1]]
    for j in range(len(u_lst)-1, -1, -1):
        s_lst[num_dict[u_lst[j]] - 1] = u_lst[j]
        num_dict[u_lst[j]] -= 1
    return s_lst


T = int(input())
for i in range(T):
    test_case = list(map(str,input().split()))
    num = test_case[0]
    size = int(test_case[1])
    unsorted_num_lst = list(map(str,input().split()))
    sorted_num_lst = [0] * size
    result = new_counting_sort(unsorted_num_lst,sorted_num_lst)
    print(num)
    for gns in result:
        print(gns,end=' ')
    print()
