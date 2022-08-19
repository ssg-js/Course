import sys

sys.stdin = open('input.txt')

# a에서 b로 가는 dfs
def dfs(a, b):
    visited[a] = True

for t in range(1, int(input()) + 1):
    nodes, edges = map(int, input().split())
    info = [[] for _ in range(nodes+1)]
    for _ in range(edges):
        a, b = map(int, input().split())
        info[a].append(b)

    start, arrive = map(int, input().split())

    visited = [False] * (nodes+1)
