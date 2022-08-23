import sys

sys.stdin = open('input.txt')


def dfs(x, y):
    global roads
    global max_roads

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and field[nx][ny] < field[x][y] and not passed[nx][ny]:
            roads += 1
            dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(n)]
    passed = [[False] * (n + 1) for _ in range(n)]

    # 최대 높이 구하기
    max_li = []
    for i in range(n):
        max_li.append(max(field[i]))
    max_height = max(max_li)

    max_roads = 0
    roads = 0
    for i in range(n):
        for j in range(n):
            if field[i][j] == max_height:
                dfs(i, j)

