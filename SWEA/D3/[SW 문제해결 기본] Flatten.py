#Flattern D3
T = 10
result = []
for i in range(T):
    dump = int(input())
    box = input()
    boxes = list(map(int,box.split()))
    for i in range(dump):
        idx1 = boxes.index(max(boxes))
        idx2 = boxes.index(min(boxes))
        boxes[idx1] -= 1
        boxes[idx2] += 1
    sum = max(boxes) - min(boxes)
    result.append(sum)

for i in range(T):
    print("#{0} {1}".format(i+1,result[i]))