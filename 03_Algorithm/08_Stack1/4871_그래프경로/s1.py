import sys

sys.stdin = open('input.txt')


# x에서 y로 가는 dfs
def dfs(x, y):
    visited[x] = True

    for node in info[x]:
        dfs(node, y)
        if node == y:
            return 1
    return 0


for t in range(1, int(input()) + 1):

    nodes, edges = map(int, input().split())
    info = [[] for _ in range(nodes+1)]

    for _ in range(edges):
        a, b = map(int, input().split())
        info[a].append(b)

    start, arrive = map(int, input().split())

    visited = [False] * (nodes+1)

    print(f'#{t} {dfs(a, b)}')