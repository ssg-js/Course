# 5207 이진 탐색

import sys
sys.stdin = open('input.txt')


def binary_search(arr, left, right):
    global cnt, side
    m = (left + right) // 2
    if b < arr[left] or b > arr[right]:         # 예외 처리
        return
    if arr[m] == b:
        cnt += 1
    elif arr[m] > b and (side % 2 + 1 == 1 or not side):
        side = 1
        binary_search(arr, left, m - 1)
    elif arr[m] < b and (side % 2 + 1 == 2 or not side):
        side = 2
        binary_search(arr, m + 1, right)


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    list_a = sorted(list(map(int, input().split())))
    list_b = list(map(int, input().split()))

    cnt = 0
    for b in list_b:
        side = 0                                # 전에 어떤 구간을 탐색했는지(왼쪽: 1, 오른쪽: 2)
        binary_search(list_a, 0, N - 1)

    print(f'#{t} {cnt}')


