# 바이러스

def dfs(v):
    passed[v] = True

    for next_v in graph[v]:
        if not passed[next_v]:
            dfs(next_v)


computers = int(input())
lines = int(input())
graph = [[] for _ in range(computers+1)]
passed = [False] * (computers + 1)

for i in range(lines):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
cnt = passed.count(True) - 1
print(cnt)
