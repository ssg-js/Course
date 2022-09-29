# DFS


def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for next_v in node_info[v]:
        if not visited[next_v]:
            dfs(next_v)


edges = list(map(int, input().split()))

node_info = [[]]

for i in range(0, len(edges), 2):
    while len(node_info) <= edges[i]:           # [[], []] -> 1번 정보 들어갈수있음
        node_info.append([])
    node_info[edges[i]].append(edges[i + 1])

    visited = [False] * (max(edges) + 1)

    print(node_info)
    print(visited)

    dfs(1)