# D2 4873.[파이썬 S/W 문제해결 기본] 반복문자 지우기
T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = [' ' for _ in range(len(word))]
    top = -1
    for char in word:
        if char == stack[top]:
            stack.pop(top)
            top -= 1
        else:
            top += 1
            stack[top] = char

    result = 0
    for j in stack:
        if j != ' ':
            result += 1
    print("#{0} {1}".format(tc, result))