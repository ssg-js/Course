def bfs(n):
    visited[n] = True
    queue = [n]
    print(n, end=' ')

    while queue:
        n = queue.pop(0)
        for next_n in graph[n]:
            if not visited[next_n]:
                visited[next_n] = True
                queue.append(next_n)
                print(next_n, end=' ')


node, edge = map(int, input().split())
info = list(map(int, input().split()))
graph = [[] for _ in range(node + 1)]

for i in range(edge):
    graph[info[2*i]].append(info[2*i+1])
    graph[info[2*i+1]].append(info[2*i])

visited = [False] * (node + 1)

bfs(1)

