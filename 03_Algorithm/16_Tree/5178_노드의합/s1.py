# 노드의 합


def postorder_sum(v):
    if v:
        postorder_sum(ch1[v])
        postorder_sum(ch2[v])
        if values[v] == 0:  # 해당 노드의 값의 0이면 자식 노드에 해당하는 값을 더함
            values[v] = values[ch1[v]] + values[ch2[v]]
            # 여기서 자식노드가 없는 경우 values[0] = 0을 더하기 때문에 문제없음


for t in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    
    values = [0] * (N + 1)  # 각 노드에 해당하는 값을 저장

    for i in range(2, N + 1):
        parent = i // 2
        if ch1[parent] == 0:
            ch1[parent] = i
        else:
            ch2[parent] = i

    for _ in range(M):
        a, b = map(int, input().split())
        values[a] = b

    postorder_sum(1)
    print(f'#{t} {values[L]}')
            
