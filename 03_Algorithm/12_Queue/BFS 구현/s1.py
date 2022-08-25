def bfs(n):



node, edge = map(int, input().split())
info = list(map(int, input().split()))
graph = [[] for _ in range(node + 1)]

for i in range(edge):
    graph[info[2*i]].append(info[2*i+1])

visited = []
queue = []

