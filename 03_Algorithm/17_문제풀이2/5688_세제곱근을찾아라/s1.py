# 5688 세제곱근을 찾아라


for t in range(1, int(input()) + 1):
    N = int(input())

    x = -1
    root = 0
    while root ** 3 <= N:
        if root ** 3 == N:
            x = root
            break
        root += 1

    print(f'#{t} {x}')