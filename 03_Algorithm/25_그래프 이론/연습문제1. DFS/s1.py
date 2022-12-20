# DFS


def DFS(arr, v):


edges = list(map(int, input().split()))

node_info = [[]]

for i in range(0, len(edges), 2):
    if len(node_info) <= edges[i]:                  # 해당 노드에 대한 정보를 처음 넣는 경우
        node_info.append([edges[i + 1]])
    else:
        node_info[edges[i]].append(edges[i + 1])

