# 1238 Contact
# bfs

def emergency_call(v, depth, visited):
    if len(last) < depth:                           # 연락 받은 순서가 같은 사람 중 제일 처음 연락 받는 경우
        last.append(infos[v])                       # infos[v] -> []
    else:
        last.extend(infos[v])

    visited.append(v)                               # 방문했는지 저장

    for next_v in infos[v]:
        if next_v not in visited:
            emergency_call(next_v, depth + 1, visited)


for t in range(1, 11):
    N, start_node = map(int, input().split())       # N : 인원 수
    data = list(map(int, input().split()))          # [from, to, from, to, ...]

    infos = {}                                      # 각 인원이 비상연락할 수 있는 노드 저장
    for i in range(0, len(data), 2):
        if not infos.get(data[i]):                  # 키(인원번호)값이 없으면
            infos[data[i]] = [data[i+1]]
        else:
            infos[data[i]].append(data[i+1])

    last = []                                       # index : depth, value : 연락받은 사람들

    emergency_call(start_node, 1, [])

    print(f'#{f} {max[last[-1]]}')
