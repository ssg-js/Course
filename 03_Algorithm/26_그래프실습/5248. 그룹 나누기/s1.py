# 5248. 그룹 나누기


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    parent = list(range(N + 1))

    for i in range(M):
        x_root, y_root = find_set(numbers[2 * i]), find_set(numbers[2 * i + 1])
        if x_root != y_root:                            # 서로소
            parent[y_root] = x_root

    team = []
    for i in range(1, N + 1):
        team.append(find_set(i))

    print(f'#{t} {len(set(team))}')


