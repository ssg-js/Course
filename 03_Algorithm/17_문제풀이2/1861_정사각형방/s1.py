# 1861 정사각형 방
# 1046 시작

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global cnt, start
    cnt += 1
    for n in range(4):                              # 그 다음 갈 수 있는 방은 무조건 1개 이하
        nx = x + dx[n]
        ny = y + dy[n]
        if 0 <= nx < N and 0 <= ny < N and (rooms[nx][ny] - rooms[x][y]) == 1:
            bfs(nx, ny)


for t in range(1, int(input()) + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    result = [0, 0]                                 # [출발 번호, 이동할 수 있는 최대 방의 개수]

    for i in range(N):
        for j in range(N):                          # 각 방에서 출발할 수 있도록
            cnt = 0
            start = rooms[i][j]                     # 시작점 저장
            bfs(i, j)

            if result[1] < cnt:
                result[0] = start
                result[1] = cnt
            elif result[1] == cnt and result[0] > start:
                result[0] = start

    print(f'#{t}', *result)






