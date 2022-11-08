# [swea] 11013. 배열 분할

# 연속된 숫자 세그룹으로 묶어서 각 그룹의 합의 최댓값과 최솟값의 차이가 최소가 되도록

# idea
# N-1 C 2
# 1. 인덱스 a, b 를 고르기 [:a], [a:b], [b:]
# 1 <= a < N - 1
# a < b < N
# 2. a, b 로 나누고 연산하기


def combination(arr, start):
    if len(arr) == 2:
        ab.append(arr[:])
        return

    for i in range(start, N):
        arr.append(i)
        combination(arr, i + 1)
        arr.pop()


for t in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    ab = []

    combination([], 1)

    subs = []
    for case in ab:
        a, b = case[0], case[1]
        part1 = numbers[:a]
        part2 = numbers[a:b]
        part3 = numbers[b:]

        part_sum = list(map(sum, [part1, part2, part3]))

        part_sum.sort()

        subs.append(part_sum[-1] - part_sum[0])

    answer = min(subs)

    print(f"#{t} {answer}")


