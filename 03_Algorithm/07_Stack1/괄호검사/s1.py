import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    gualhos = input()

    stack = []
    result = -1
    for gualho in gualhos:
        # 여는 괄호가 나오는 경우
        if gualho == '(':
            stack.append(gualho)
        # 닫는 괄호가 나오는 경우
        else:
            if not stack:
                break
            # 여는 괄호 하나 제거
            else:
                stack.pop()
    else:  # 문제없이 다 검사 했을때
        if not stack:  # 스택이 비어있으면 짝이 맞다는 것
            result = 1

    print(f'#{t} {result}')