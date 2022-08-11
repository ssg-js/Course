import sys

sys.stdin = open('input.txt')

for t in range(1, 10 + 1):
    ladder = []
    for i in range(100):
        li = list(map(int, input().split()))
        ladder.append(li)
    out = 0
    for j in range(100):
        if ladder[99][j] == 2:
            out = j
            break
    print(out)
    # 위로 이동하면서 좌우로 길이 있으면 우선으로 이동, 아래 x
    # [좌, 우, 상, 하]
    d = [-1, 1, -1, 0]

    i = 100
    j = out
    while True:
        for di in range(4):
            if di < 2:
                if j + d[di] == 1:
                    j += d[di]
                    break
            else:
                i += d[di]
                break

        if i == 0:
            break

    start = j
    print(f'#{t} {start}')
