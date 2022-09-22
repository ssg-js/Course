# 연습문제2. baby gin


def baby_gin(arr):
    num = 0
    result = False
    for i in range(0, len(arr), 3):
        if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]: # triplet인 경우
            num += 1
        elif arr[i] + 1 == arr[i+1] and arr[i+1] + 1 == arr[i+2]:   # run인 경우
            num += 1
    if num == 2:
        result = True

    return result


n = int(input())
numbers = [sorted(list(map(int, input()))) for _ in range(n)]

cnt = 0      # run, triplet 카운트 -> 2면 baby-gin

for number in numbers:
    print(baby_gin(number))



