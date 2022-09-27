# 퀵 정렬


def partition(arr, left, right):
    pivot = arr[left]
    i, j = left, right

    while i <= j:
        while i <= j and pivot >= arr[i]:
            i += 1
        while i <= j and pivot <= arr[j]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]           # j < i 일 때

    return j


def quick_sort(arr, left, right):   
    if left < right:                                # 종료 조건
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


for t in range(1, int(input()) + 1):
    N = int(input())
    li = list(map(int, input().split()))

    quick_sort(li, 0, N - 1)

    print(f'#{t} {li[N // 2]}')
