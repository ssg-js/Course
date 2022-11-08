# 11725 트리의 부모 찾기
# 1626시작
# 간선 정보들을 가지고 각 노드별 어떻게 연결되어있는지 만들기


N = int(input())
infos = [list(map(int, input().split())) for _ in range(N-1)]
root = 1


ch1 = [0] * (N + 1)
ch2 = [0] * (N + 1)

edges = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
for info in infos:      # 간선 정보 노드별 저장
    a, b = info[0], info[1]
    edges[a].append(b)
    edges[b].append(a)

for i in range(N + 1):  # 각 노드별 차일드 저장
    for node in edges[i]:
        if not ch1[i]:  # 첫 자식 비었으면
            ch1[i] = node
            parents[node] = i
        else:
            ch2[i] = node
            parents[node] = i

for parent in parents[2:]:
    print(parent)


