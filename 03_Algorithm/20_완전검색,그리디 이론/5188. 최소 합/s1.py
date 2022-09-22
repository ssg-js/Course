# 5188. 최소합


def min_sum(x, y, hap):
    hap += board[x][y]
    if min_value and hap > min(min_value):        # 가지치기
        return
    if x == N - 1 and y == N - 1:
        min_value.append(hap)
        return
    if x + 1 < N:
        min_sum(x + 1, y, hap)

    if y + 1 < N:
        min_sum(x, y + 1, hap)


for t in range(1, int(input()) + 1):
    N = int(input())                            # 가로세로 칸 수
    board = [list(map(int, input().split())) for _ in range(N)]

    min_value = []
    min_sum(0, 0, 0)

    print(f'#{t} {min(min_value)}')



