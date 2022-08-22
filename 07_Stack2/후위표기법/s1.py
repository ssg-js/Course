# 후위표기법 : 연산자를 피연산자 뒤에 표기하는 방법
import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    cal = input()
    result = ''
    stack = []
    for v in cal:
        if v.isdigit():
            result += v
        else:
            if not stack:
                stack.append(v)
            elif v == ')':
                while stack:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    result += stack.pop()
            elif v == '*' or v == '/':
                while stack and stack[-1] != '(':
                    if stack[-1] == '+' or stack[-1] == '-':
                        stack.append(v)
                        break
                    result += stack.pop()
            else:  # +, - 일 때
                while stack and stack[-1] != '(':
                    if stack[-1] == '+' or stack[-1] == '-':
                        stack.append(v)
                        break
                    result += stack.pop()

    while stack:
        if stack[-1] == '(':
            stack.pop()
        else:
            result += stack.pop()

    print(f'#{t} {result}')
