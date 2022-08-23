# 괄호 검사
import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    text = input()

    result = 0
    stack = []
    for s in text:
        if s == '(' or s == '{':
            stack.append(s)

        if stack and s == ')' and stack[-1] == '(':
            stack.pop()
        elif stack and s == '}' and stack[-1] == '{':
            stack.pop()
        elif s == ')' or s == '}':
            stack.append(0)

    if not stack:
        result = 1

    print(f'#{t} {result}')