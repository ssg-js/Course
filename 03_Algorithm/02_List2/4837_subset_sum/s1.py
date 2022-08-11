import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    array = [i for i in range(1, 13)]
    a = len(array)

    count = 0
    for i in range(1 << a):
        # 원소의 개수를 알기 위해 2진수에서 1의 개수를 구함
        one_count = 0
        elements = i
        for _ in range(a):
            if elements & 1:
                one_count += 1
            elements = elements >> 1
            if elements == 0:
                break
        if one_count == n:
            element_sum = 0
            for j in range(a):
                if i & (1 << j):
                    element_sum += array[j]
            if element_sum == k:
                count += 1

    print(f'#{t} {count}')