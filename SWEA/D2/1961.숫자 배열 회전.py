# D2 숫자 배열 회전


def spin(lst):
    size = len(lst)
    spin_lst = [[0]*size for _ in range(size)]
    for column in range(size):
        for row in range(size):
            spin_lst[column][row] = lst[size-row-1][column]
    return spin_lst


T = int(input())
for i in range(T):
    length = int(input())
    org_list = []
    for j in range(length):
        temp =list(map(int,input().split()))
        org_list.append(temp)
    spin1 = spin(org_list)
    spin2 = spin(spin1)
    spin3 = spin(spin2)
    tp = [spin1,spin2,spin3]
    print_list = []
    for j in range(length):
        temp = []
        for k in range(len(tp)):
            for _ in range(length):
                temp.append(tp[k][j][_])
            temp.append(" ")
        print_list.append(temp)
    print("#{}".format(i + 1))
    for j in range(length):
        for k in range(len(print_list[0])):
            print(print_list[j][k],end='')
        print()