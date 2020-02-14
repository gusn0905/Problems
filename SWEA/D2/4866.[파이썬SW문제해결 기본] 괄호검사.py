# D2 4866.[파이썬 SW 문제해결 기본] 괄호검사
T = int(input())
for tc in range(1, T+1):
    temp = input()
    sentence = list(temp)
    stack = [0] * 100
    top = -1
    for char in sentence:
        if char == '(' or char == '{':
            top += 1
            stack[top] = char
        elif char == ')':
            if stack[top] != 0 and stack[top] == '(':
                stack[top] = 0
                top -= 1
            else:
                stack[top] = char
                break
        elif char == '}':
            if stack[top] != 0 and stack[top] == '{':
                stack[top] = 0
                top -= 1
            else:
                stack[top] = char
                break
    if stack.count(0) != 100:
        result = 0
    else:
        result = 1
    if '(' not in sentence and '{' not in sentence and ')' not in sentence and '}' not in sentence:
        result = 1
    print("#{0} {1}".format(tc, result))