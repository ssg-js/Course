import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n, m = input().split()
    pic = [list(map(int, input().split())) for _ in range(n)]

    # [우, 좌]
    dx = [0, 1, 0, -1]
    # [상, 하]
    dy = [1, 0, 1, 0]

    max_seq = 0

    for i in range(n):
        for j in range(m):
            if pic[i][j] == 1:
                seq = 1
                for di in range(4):
                    x = dx[di] + j
                    y = dy[di] + i
                    # 위, 아래로 연속된 1의 개수
                    if 0 <= y < n:
                        while pic[y][j]:
                            if pic[y+dy[di]][i]:
                                seq += 1

                            else:
                                break
                    # 좌, 우로 연속된 1의 개수
                    if 0 <= x < m:
                        while pic[i][x]:

                    if seq > max_seq:
                        max_seq = seq


