# D2 가랏 RC카
T = int(input())
result = []
for i in range(T):
    sec = int(input())
    distance = 0
    command = [0, 0]
    for v in range(sec):
        com = input()
        temp = list(map(int,com.split()))
        if temp[0] == 0:
            command[0] = 0
        else:
            command[0] = temp[0]
            if command[0] == 1:
                command[1] += temp[1]
            elif command[0] == 2:
                if command[1] < temp[1]:
                    command[1] = 0
                else:
                    command[1] -= temp[1]
        distance += command[1]
    result.append(distance)

for i in range(T):
    print("#{0} {1}".format(i+1,result[i]))