
for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    counter = [0] * (N + 1)

    for number in numbers:
        counter[number] += 1

    cnt = 0
    result = 0
    for i, c in enumerate(counter):
        if c:
            cnt += 1
        if cnt == K:
            result = i
            break
    print(f'#{t} {result}')
