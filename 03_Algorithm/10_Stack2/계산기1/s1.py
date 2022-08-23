# 계산기1

calculation = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

fomula = input()
stack = []
for char in fomula:
    if char not in '*/+-':
        stack.append(int(char))
    else:
        x = stack.pop()
        y = stack.pop()
        stack.append(calculation[char](x, y))

print(stack.pop())
