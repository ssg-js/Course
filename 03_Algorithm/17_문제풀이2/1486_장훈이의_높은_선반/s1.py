# 1486 장훈이의 높은 선반


for t in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    results = []                    # B를 넘는 높이와 B의 차를 저장할 리스트

    for i in range(1, 1 << N):      # i : 1, 10, 11, 100, ...
        heights_sum = 0
        for j in range(N):
            if i & (1 << j):        # j : 1, 10, 100, 1000, ...
                heights_sum += H[N-1-j]

        result = heights_sum - B
        if result >= 0:              # (쌓은 높이) >= B
            results.append(result)

    print(f'#{t} {min(results)}')
