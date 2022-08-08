import sys

sys.stdin = open("input.txt")

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    result = 0

    for i in range(n):
        max_height = 0

        for j in range(i + 1, n):
            if numbers[i] > numbers[j]:
                max_height += 1

        if result < max_height:
            result = max_height

    print(f'#{test_case} {result}')