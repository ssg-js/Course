# 암호생성기

cycle = 5

for t in range(1, 10 + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    while 0 not in numbers:
        for i in range(1, cycle + 1):
            a = numbers.pop(0)
            if a-i <= 0:
                numbers.append(0)
                break
            numbers.append(a-i)

    print(f'#{n}', *numbers)

