# BOJ_1753. 최단경로 (다익스트라)
# 틀림

# 출발 정점에서 다른 정점들까지의 최단 거리를 출발정점 기준으로 리스트에 저장
# 출발 점정에서 다른 정점들가지의 거리 저장하는 리스트 만들기
# 다익스트라
# 방문 처리 리스트 만들기
# 해당 정점 방문 처리
# 시작하는 정점까지의 거리 0으로 저장
# 출발 정점에서 주변 정점까지의 거리 초기화
# 시작 정점을 제외한 나머지 정점들에 대해서 반복
# 최단거리가 확정(방문처리가 false인 점들)되지 않은 정점들 중 최단 거리가 가장 짧은 정점을 선택
# 해당 정점 최단 거리 확정
# 해당 정점까지의 누적거리 계산하면서 기존 값보다 작으면 갱신


def dijkstra(start):
    visited = [False] * (V + 1)
    visited[start] = True
    distance[start] = 0

    for end, cost in graph[start]:                  # 시작 정점에서 주변 정점까지의 정리 정리
        distance[end] = cost

    for _ in range(V - 1):
        min_dist = INF
        for i in range(1, V + 1):
            if not visited[i] and min_dist > distance[i]:
                min_node = i
                min_dist = distance[i]

        visited[min_node] = True

        for next_node, dist in graph[min_node]:     # 해당 정점에 인접한 노드 정보들
            new_dist = distance[min_node] + dist
            if distance[next_node] > new_dist:
                distance[next_node] = new_dist


V, E = map(int, input().split())                    # 정점의 개수 V, 간선의 개수 E
K = int(input())                                    # 시작 정점 K
graph = [[] for _ in range(V + 1)]
INF = 999999
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())             # u -> v, 가중치 w
    graph[u].append((v, w))

dijkstra(K)
for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])





