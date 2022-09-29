# 최소신장트리(MST), 최단경로(다익스트라)

### 최소신장트리(MST, Minimum Spanning Tree)

- 어떤 그래프에서 **모든 노드를 포함하지만 사이클은 없는** 간선의 비용이 가장 낮은 그래프

- 이어져만 있으면 됨 -> 집합

- 노드에서 greedy하게 진행(이게 최소라고 증명됨)

- 대표값 확인 (경로 압축하면서 parent 갱신) -> 서로소인 집합들 Union 

- 크루스칼 -> 서로소집합(Union-Find)
  
  - Union-Find
    
    - 서로소집합, 상호베타집합, disjoint set
    
    - **Find**(membership 연산(in, not in)), **Union**(합집합)
    
    - 알고리즘보다는 자료구조에 가까움
    
    - 세가지 메서드 : make_set, find_set(대표값 출력), union
    
    - 트리로 집합을 표현 
    
    - parent(각 숫자가 속해있는 집합의 대표값)을 이용
    
```python
# 1. 반복문
def find_set(node):
    while node != parent[node]:
    node = parent[node]
        return node
    
    # # 2. 재귀
    # def find_set(node):
    #     if node != parent[node]:
    #         return find_set(parent[node])
    #     return node
    
    
    # # 3. 재귀 - 경로 압축(부모 노드를 대표값으로 만듦)
    # def find_set(node):
    #     if node != parent[node]:
    #         parent[node] = find_set(parent[node])
    #     return parent[node]
    
    
    n, m = map(int, input().split())  # 정점, 간선(Union 횟수) 개수
    parent = list(range(n + 1))
    
    for _ in range(m):
        x, y = map(int, input().split())
        x_root, y_root = find_set(x), find_set(y)  # Find
    
        # Union
        if x_root != y_root:  # 서로소 집합인 경우만 합집합 연산
            if x_root < y_root:
                parent[y_root] = x_root
            else:
                parent[x_root] = y_root
    
    # 출력
    for i in range(1, n + 1):
        print(find_set(i), end=' ')
    
    print()
    print(parent)

```



- 프림
  
  - 현재 **정점** 중 가장 최소의 값
  
  - 임의의 정점 선택 -> MST에서 갈 수 있는 모든 정점 중에 가장 최소 비용 선택
  
  - visited(방문 여부 -> 포함 여부)와 distance(각 정점으로 가는 최솟값)
    
```python
# 1) 일반적인 프림 알고리즘

def prim(start):
    visited = [False] * (n + 1)  # MST에 포함 여부 리스트
    distance = [INF] * (n + 1)  # distance[v] => 정점 v가 MST에 속한 정점과 연결된 간선의 비용
    distance[start] = 0
    cost = 0  # MST의 비용 총합(== 최소 비용)

    # 정점의 개수만큼 반복하면서 모든 정점을 이은 MST 생성
    for _ in range(n):
        # 1. MST의 정점에서 이동할 수 있는 모든 정점 중 가장 적은 비용으로 이동 가능한 정점 찾기(Greedy)
        min_dist = INF
        for i, dist in enumerate(distance):
            if not visited[i] and dist < min_dist:
                min_node = i
                min_dist = dist

        # 2. 해당 정점을 MST에 포함하고 비용을 더함
        visited[min_node] = True
        cost += min_dist

        # 3. 해당 정점과 인접한 정점에 대해 최소 비용 갱신
        for next_node, dist in graph[min_node]:
            if not visited[next_node] and dist < distance[next_node]:
                distance[next_node] = dist

    return cost


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 나올 수 없는 임의의 큰 수

for _ in range(m):
    s, e, w = map(int, input().split())  # 시작 정점, 도착 정점, 비용
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))  # 1번 정점에서 시작
```



- 힙 : 안에가 어떻게 되있든 pop()하면 최솟값이 나옴
  
  - 우선순위 큐 : 우선순위에 따라 pop() -> 힙과 비스무래함
  
  - 파이썬에서는 **heapq**라는 모듈이 있음
    
```python
# 2) 힙을 이용한 프림 알고리즘

from heapq import heappush, heappop


def prim(start):
      visited = [False] * (n + 1)  # MST에 포함 여부 리스트
      heap = [(0, start)]  # 힙 선언 [(비용, 정점)]
      cost = 0  # MST의 가중치 총합(== 최소 비용)

      while heap:
          # 1. 가장 적은 비용으로 이동 가능한 정점 찾기(Greedy)
          min_dist, min_node = heappop(heap)  # 최소힙이므로 튜플의 첫 번째 원소를 기준으로 최소값 pop
          if visited[min_node]:
              continue  # 이미 MST에 포함된 정점이라면 무시

          # 2. 해당 정점을 MST에 포함하고 비용 총합을 더함
          visited[min_node] = True
          cost += min_dist

          # 3. 해당 정점과 인접한 정점에 대해 heappush
          for next_node, dist in graph[min_node]:
              if not visited[next_node]:
                  heappush(heap, (dist, next_node))

      return cost


  n, m = map(int, input().split())  # 정점, 간선 개수
  graph = [[] for _ in range(n + 1)]

  for _ in range(m):
      s, e, w = map(int, input().split())  # 시작 정점, 도착 정점, 비용
      graph[s].append((e, w))
      graph[e].append((s, w))

  print(prim(1))  # 1번 정점에서 시작
```



#### 그럼 크루스칼과 프림은 도대체 언제쓰냐???

- 크루스칼은 간선 위주라 간선이 많을 때 불리함 -> 프림 사용

- 정점이 많은 경우에는 크루스칼로 풀기!!!

### 다익스트라

- 그래프 탐색 알고리즘

- 특정 정점 -> 다른 모든 정점 최단거리

- 음의 간선 X, 그리디 알고리즘

- distance(간선의 값이 누적됨)
  
```python
# 1) 일반적인 다익스트라 알고리즘

def dijkstra(start):
    visited = [False] * (n + 1)  # 방문 처리 리스트(최단 거리가 확정된 정점)
    visited[start] = True
    distance[start] = 0

    # 시작 정점과 인접한 정점에 대해 최단 거리 초기화
    for e, w in graph[start]:
        distance[e] = w

    # 시작 정점을 제외한 나머지 정점에 대해서만 반복하므로 n - 1 번 반복함
    for _ in range(n - 1):
        # 1. 최단 거리가 확정되지 않은 정점들 중 최단 거리가 가장 짧은 정점을 선택
        min_dist = INF
        for i in range(1, n + 1):
            if not visited[i] and min_dist > distance[i]:
                min_node = i
                min_dist = distance[i]

        # 2. 해당 정점 최단 거리 확정
        visited[min_node] = True

        # 3. 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for next_node, dist in graph[min_node]:
            new_dist = distance[min_node] + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist



n, m = map(int, input().split()) # 정점, 간선 개수
 graph = [[] for _ in range(n + 1)]
 INF = 99999999 # 나올 수 없는 임의의 큰 수
 distance = [INF] * (n + 1) # 출발 정점에서 다른 정점들까지의 최단 거리(무한으로 초기화)

for _ in range(m):
 s, e, w = map(int, input().split())
 graph[s].append((e, w))

dijkstra(1) # 1번 정점에서 시작
 print(distance)
```

 

- 힙을 이용한 다익스트라 알고리즘

```python
# 2) 힙을 이용한 다익스트라 알고리즘

from heapq import heappush, heappop


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]  # 힙 선언 [(비용, 정점)]

    while heap:
        # 1. 최단 거리가 가장 짧은 정점을 선택
        min_dist, min_node = heappop(heap)

        # 2. 이미 최단 거리로 기록되어 있는 값보다 높은 경우 무시
        if min_dist > distance[min_node]:
            continue

        # 3. 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 나올 수 없는 임의의 큰 수
distance = [INF] * (n + 1)  # 출발 정점에서 다른 정점들까지의 최단 거리(무한으로 초기화)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dijkstra(1)  # 1번 정점에서 시작
print(distance)
```
