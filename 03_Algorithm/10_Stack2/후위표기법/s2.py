# 후위표기법 : 연산자를 피연산자 뒤에 표기하는 방법
import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    cal = input()
    result = ''
    stack = []
    for v in cal:
        # 숫자는 그냥 저장
        if v.isdigit():
            result += v
        else:
            # 스택이 비어있으면 바로 저장
            if not stack or v == '(':
                stack.append(v)
            # 닫는 괄호만나면 여는 괄호 만날때까지 pop해서 출력에 저장
            elif v == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
            # * / 만나면 스택 안에 낮은연산자(+, -)을 만날때까지 팝
            elif v in '*/':
                # 수정 전
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(v)
            elif v in '+-':  # +, - 일 때
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(v)

    while stack:
        result += stack.pop()

    print(f'#{t} {result}')
