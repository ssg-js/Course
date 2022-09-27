# 5204 병합 정렬


def merge(left, right):
    global cnt
    i, j = 0, 0
    arr = []

    if left[-1] > right[-1]:                # 경우의 수 카운트
        cnt += 1

    while i < len(left) and j < len(right):
        if right[j] < left[i]:
            arr.append(right[j])
            j += 1
            continue
        arr.append(left[i])
        i += 1

    arr.extend(left[i:])
    arr.extend(right[j:])

    return arr


def merge_sort(arr):
    if len(arr) <= 1:                       # 종료 조건
        return arr

    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])     # 왼쪽
    right_arr = merge_sort(arr[middle:])    # 오른쪽

    return merge(left_arr, right_arr)       # 병합


for t in range(1, int(input()) + 1):
    N = int(input())
    li = list(map(int, input().split()))   
    
    cnt = 0                                 # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우

    merged = merge_sort(li)

    print(f'#{t} {merged[N // 2]} {cnt}')
