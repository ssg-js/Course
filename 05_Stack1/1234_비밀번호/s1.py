import sys

sys.stdin = open('input.txt')


def no_repeat(num):
    stack = []
    for v in num:
        if stack and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
    return stack


for t in range(1, 10 + 1):
    n, numbers = input().split()
    numbers = list(map(int, numbers))
    while True:
        if numbers == no_repeat(numbers):
            break
        numbers = no_repeat(numbers)

    print(f'#{t} ', *numbers, sep='')