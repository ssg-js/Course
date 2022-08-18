import sys

sys.stdin = open('input.txt')


def no_repeat(s):
    stack = []
    for v in s:
        if stack and stack[-1] == v:
                stack.pop()
        else:
            stack.append(v)
    return stack


for t in range(1, int(input()) + 1):
    text = list(map(str, input()))
    while True:
        if text == no_repeat(text):
            break
        text = no_repeat(text)

    print(f'#{t} {len(text)}')