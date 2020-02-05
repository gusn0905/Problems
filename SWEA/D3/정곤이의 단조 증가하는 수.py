# 정곤이의 단조 증가하는 수
def monoInc(num):
    cnt = 0
    nums = str(num)
    if len(nums) == 1:
        return True
    for c in range(len(nums)-1):
        if nums[c] <= nums[c+1]:
            cnt += 1
    if cnt == (len(nums) -1):
        return True
    else:
        return False


T = int(input())
for i in range(T):
    size = int(input())
    num_list = list(map(int,input().split()))
    mul_list = []
    for j in range(size):
        for k in range(j+1,size):
            temp = num_list[j] * num_list[k]
            mul_list.append(temp)
    final_list = []
    for j in range(len(mul_list)):
        if monoInc(mul_list[j]):
            final_list.append(mul_list[j])
    result = 0
    if len(final_list) == 0:
        result = -1
    else:
        result = max(final_list)
    print("#{0} {1}".format(i+1,result))