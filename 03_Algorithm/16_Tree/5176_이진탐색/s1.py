# 5176 이진 탐색


def inorder(v):
    global value
    if v:
        inorder(ch1[v])
        numbers[v] = value
        value += 1
        inorder(ch2[v])


for t in range(1, int(input()) + 1):
    N = int(input())

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    numbers = [0] * (N + 1)         # 각 노드의 값

    value = 1
    for n in range(2, N + 1):
        parent = n // 2             # 부모 노드 인덱스
        if ch1[parent] == 0:
            ch1[parent] = n
        else:
            ch2[parent] = n

    inorder(1)
    print(f'#{t} {numbers[1]} {numbers[N//2]}')
