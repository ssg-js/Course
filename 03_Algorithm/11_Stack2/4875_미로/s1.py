# 미로

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dfs(a, b):
    global result
    visited[a][b] = True

    for d in range(4):
        ni = a + di[d]
        nj = b + dj[d]

        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
            if maze[ni][nj] == 3:
                result = 1
                break
            elif maze[ni][nj] == 0:
                dfs(ni, nj)


for t in range(1, int(input()) + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    result = 0
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                dfs(i, j)

    print(f'#{t} {result}')



