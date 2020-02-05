# D2 패턴 마디의 길이
T = int(input())
result = []
for i in range(T):
    word = input()
    for t in range(1,len(word)):
        if word[:t] == word[t:2*t]:
            print(t)
            result.append(t)
            break
for i in range(T):
    print("#{0} {1}".format(i+1, result[i]))