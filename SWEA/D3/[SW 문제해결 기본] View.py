#1206. View D3
T = 10
result = []
for i in range(T):
    num = int(input())
    height = input()
    building = list(map(int,height.split()))
    sum = 0
    for j in range(2,len(building)):
        for k in range(building[j],0,-1):
            if k > building[j-2] and k > building[j-1] and k > building[j+1] and k > building[j+2]:
                sum += 1
    result.append(sum)

for i in range(T):
         print("#{} {}".format(i+1,result[i]))