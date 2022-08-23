import sys

sys.stdin = open('input.txt')

for t in range(1, 10 + 1):
    tc = int(input())
    # 한줄 씩 미로 모양받기
    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))
    # 출구 구하기
    out = 0
    for j in range(100):
        if ladder[99][j] == 2:
            out = j
            break
    # 위로 이동하면서 좌우로 길이 있으면 우선으로 이동, 아래 x
    # [좌, 우]
    d = [-1, 1]

    i = 99
    j = out
    while i > 0:
        for di in range(2):
            if 0 <= j + d[di] < 100:
                if ladder[i][j + d[di]] == 1:
                    j += d[di]
                    while ladder[i-1][j] == 0:
                        j += d[di]
                    break
        i -= 1

    start = j
    print(f'#{t} {start}')
