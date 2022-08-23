import sys

sys.stdin = open('input.txt')

t = 10

for tc in range(1, t + 1):
    n = int(input())
    arr = list()
    for i in range(100):
        li = list(map(int, input().split()))
        arr.append(li)

    max_sum = 0
    diagonal_sum_r = 0
    diagonal_sum_l = 0

    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            if i == 99-j:
                diagonal_sum_l += arr[i][j]
        if row_sum > max_sum:
            max_sum = row_sum

        column_sum = 0
        for j in range(100):
            column_sum += arr[j][i]
            if i == j:
                diagonal_sum_r += arr[i][j]
        if column_sum > max_sum:
            max_sum = column_sum
    if diagonal_sum_r > max_sum:
        max_sum = diagonal_sum_r
    elif diagonal_sum_l > max_sum:
        max_sum = diagonal_sum_l

    print(f'#{n} {max_sum}')