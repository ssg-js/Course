# 연습문제1. 선택정렬


def select_sort(arr, s):
    n = len(arr)
    if s == n - 1:
        return
    min_index = s
    for i in range(s, n):
        if arr[min_index] > arr[i]:
            min_index = i                       # 최소값 index 저장
    arr[s], arr[min_index] = arr[min_index], arr[s]         # 자리 바꿔주기

    select_sort(arr, s + 1)


arr = [2, 4, 6, 1, 9, 8, 7, 0]
select_sort(arr, 0)
print(arr)