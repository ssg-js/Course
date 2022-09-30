# 5249. 최소 신장 트리
# 크루스칼


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    edges = []

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))

    edges.sort()

    parent = list(range(V + 1))
    count = 0                                           # 간선 개수만큼 세려구
    cost = 0                                            # 가중치 총합

    for dist, x, y in edges:
        root_x, root_y = find_set(x), find_set(y)

        if root_x != root_y:                            # 서로소
            parent[root_y] = root_x
            count += 1
            cost += dist

            if count > E:
                break

    print(f'#{t} {cost}')




