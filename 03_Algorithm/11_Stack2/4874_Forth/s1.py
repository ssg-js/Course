# Forth
import sys
sys.stdin = open('input.txt')

calculation = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}

for t in range(1, int(input()) + 1):
    word = input().split()

    stack = []
    for char in word:
        if char == '.':
            if len(stack) != 1:
                print(f'#{t} error')
                break
            print(f'#{t} {stack[0]}')
        elif char not in '*/+-':
            stack.append(int(char))
        elif stack:
            try:
                x = stack.pop()
                y = stack.pop()
                stack.append(calculation[char](y, x))
            except:
                print(f'#{t} error')
                break



