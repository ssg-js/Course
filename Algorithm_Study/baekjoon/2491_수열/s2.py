# 수열
# 미완성

# 연속해서 키지는 것 또는 연속해서 작아지는 것 중 가장 긴 것 찾기
# 같은 것도 가능

# idea
# 각 숫자들로 시작하면서 연속해서 작아지거나 커지는 개수 세기


N = int(input())
numbers = list(map(int, input().split()))
cnt_max = 0

for i, number in enumerate(numbers):
    if cnt_max > (N - i):
        break

    cnt = 1
    now = i
    while now < N - 1:          # 연속해서 커지기
        if numbers[now] == numbers[now + 1]:
            cnt += 1
            now += 1
        elif numbers[now] < numbers[now + 1]:
            while now < N - 1:
                if numbers[now] > numbers[now + 1]:
                    break
                now += 1
                cnt += 1


