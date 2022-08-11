import sys

sys.stdin = open('input.txt')


t = int(input())

for tc in range(1, t + 1):
    num_set = list(map(int, input().split()))

    n = len(num_set)
    zero = 0

    # 0일때는 빼고 부분집합의 원소의 합을 구해서 0인지 아닌지 판별
    for i in range(1, 1 << n):
        elements_sum = 0
        # 각 원소 하나씩 비교하기 위해서 n번 반복
        for j in range(n):
            #  1 << j : 1, 10, 100, ...
            if i & (1 << j):
                # 1 << j에 따라 맨 오른쪽 요소부터 비교하게(편하게)
                elements_sum += num_set[n - 1 - j]
                
        if elements_sum == 0:
            zero = 1
            break

    print(f'#{tc} {zero}')
