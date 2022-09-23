# 4615. 재미있는 오셀로 게임
# 1: 흑돌, 2: 백돌
# 입력에 따라 돌을 놓고
# 방향 설정하면 그 방향에 흰돌이 연속되어 있고 흑돌이 나오는지 검사하기

import sys
sys.stdin = open('input.txt')

dx = [1, 1, 0, -1, -1, -1, 0, 1]                             # 극좌표계 돌듯이
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    i = N // 2
    board[i-1][i], board[i][i-1], board[i-1][i-1], board[i][i] = 1, 1, 2, 2

    for p in range(M):
        i, j, stone = map(int, input().split())             # 위치와 돌정보
        i -= 1                                              # 리스트 맞춰서 바꾸기
        j -= 1
        board[i][j] = stone                                 # 돌 놓기
        other_stone = (stone % 2) + 1                       # 내돌과 다른돌
        for di in range(8):                                 # 무려 8방위
            nx, ny = i, j
            others = []                                     # 해당 방향 상대방돌 좌표 저장
            while True:
                nx = nx + dx[di]                            # 방향 정해서 탐색
                ny = ny + dy[di]
                if 0 <= nx < N and 0 <= ny < N:             # 방향 정했으
                    if board[nx][ny] == 0 or (board[nx][ny] == stone and not others):   # 빨리 다른 방향 넘기기
                        break
                    elif board[nx][ny] == other_stone:                                  # 상대방돌 좌표저장
                        others.append([nx, ny])
                    elif board[nx][ny] == stone and others:                             # 상대방돌 뒤집기가능
                        for coordinate in others:
                            a, b = coordinate[0], coordinate[1]
                            board[a][b] = stone
                        break                                                           # 나가기
                else:
                    break                                                                   # 오바되는 경우

    result = [0, 0]                                         # 흑돌, 백돌 개수 저장
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                result[0] += 1
            elif board[i][j] == 2:
                result[1] += 1

    print(f'#{t}', *result)
