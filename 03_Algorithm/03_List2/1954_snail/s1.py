import sys

sys.stdin = open('input.txt')


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    # int는 immutable이라 깊은 복사, list는 mutable이라 얉은 복사(-> for문으로 해결)
    snail = [[0] * n for _ in range(n)]

    # [우, 하, 좌, 상]
    d = [1, 1, -1, -1]
    
    # 오른쪽 먼저 시작
    di = 0
    # 현재 위치
    i = 0
    j = 0
    # 숫자
    num = 1
    # 더 채울 곳이 있으면 1, 채울 곳이 없으면 0
    go_on = 1

    while go_on:
        # 해당 위치에 숫자 지정
        snail[i][j] = num
        num += 1
        go_on = 0

        # 4방위만 돌고 나오도록
        for _ in range(4):
            # 좌, 우인 경우
            if di % 2 == 0:
                if (0 <= j + d[di] < n) and not snail[i][j + d[di]]:
                    j += d[di]
                    # 다음 공간이 있으므로 1
                    go_on = 1
                    break
                else:
                    di = (di + 1) % 4

            # 상, 하인 경우
            else:

                if (0 <= i + d[di] < n) and not snail[i + d[di]][j]:
                    i += d[di]
                    # 다음 공간이 있으므로 1
                    go_on = 1
                    break
                else:
                    di = (di + 1) % 4

    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=' ')
        print()