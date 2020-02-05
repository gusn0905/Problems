# D2 파스칼 삼각형
T = int(input())
for i in range(T):
    print("#{}".format(i+1))
    height = int(input())
    pascal = [[1]*k for k in range(1,height+1)]
    for row in range(2,len(pascal)):
        for column in range(1,len(pascal[row])-1):
            pascal[row][column] = pascal[row-1][column-1] + pascal[row-1][column]

    for j in range(len(pascal)):
        for k in range(len(pascal[j])):
            print(pascal[j][k], end=' ')
        print()