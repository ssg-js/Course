# 퀵정렬


def partition(arr, left, right):
    pivot = arr[left]                           # 피벗
    i, j = left, right

    while i <= j:
        while i <= j and arr[i] <= pivot:       # 피벗보다 작으면 쭉 이동
            i += 1
        while i <= j and arr[j] >= pivot:       # 피벗보다 크면 쭉 이동
            j -= 1

        if i < j:                               #
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    return j


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


for t in range(1, int(input()) + 1):
    li = list(map(int, input().split()))

    quick_sort(li, 0, len(li) - 1)

    print(li)