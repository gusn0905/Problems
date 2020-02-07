#D3 5356. 의석이의 세로로 말해요
T = int(input())
for i in range(T):
    words = []
    for j in range(5):
        temp = input()
        tp = list(temp)
        words.append(tp)
    length = len(words[0])
    for j in range(1,5):
        if len(words[j]) > length:
            length = len(words[j])
    for j in range(5):
        if len(words[j]) < length:
            for k in range(length-len(words[j])):
                words[j].append('')
    result = []
    for c in range(length):
        for r in range(5):
            if words[r][c] != '':
                result.append(words[r][c])
    final = ''.join(result)
    print("#{0} {1}".format(i+1,final))