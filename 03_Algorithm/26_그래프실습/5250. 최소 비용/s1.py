# 5250. 최소 비용\
# 각 좌표별 연료 소비량을 리스트에 저장


def dijkstra(x, y):
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    distance[x][y] = 0

    for near_x, near_y, f in heights[x][y]:
        distance[near_x][near_y] = f




dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for t in range(1, int(input()) + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]
    INF = 99999999
    distance = [[INF] * N for _ in range(N)]

    edges = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if heights[nx][ny] - heights[i][j] <= 0:        # 연료 1
                        fuel = 1
                    else:
                        fuel = heights[nx][ny] - heights[i][j]      # 연료 마니
                    edges[i][j].append((nx, ny, fuel))

