# DFS
import sys

sys.stdin = open('input.txt')


def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


points, lines = map(int, input().split())
graph_info = list(map(int, input().split()))
graph = [[] for _ in range(points+1)]
visited = [False] * (points + 1)

for i in range(0, len(graph_info), 2):
    a, b = graph_info[i], graph_info[i+1]
    graph[a].append(b)
    graph[b].append(a)

dfs(1)