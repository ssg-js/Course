import sys

sys.stdin = open('input.txt')


def dfs(x, y):
    global total
    total += 1
    visited[x][y] = True

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())
board = []
for _ in range(n):
    li = list(map(int, input()))
    board.append(li)

visited = [[False] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            total = 0
            dfs(i, j)
            result.append(total)

result.sort()
print(len(result), *result, sep='\n')