# 5174 subtree


def search(v):
    global cnt
    if v:
        cnt += 1
        search(ch1[v])
        search(ch2[v])


for t in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    L = max(edges)
    ch1 = [0] * (L + 1)     # 왼쪽 아이
    ch2 = [0] * (L + 1)     # 오른쪽 아이

    cnt = 0                 # 서브트리 노드 개수 세는 아이
    for i in range(0, 2 * E, 2):
        a, b = edges[i], edges[i+1]
        if ch1[a] == 0:
            ch1[a] = b
        else:
            ch2[a] = b

    search(N)

    print(f'#{t} {cnt}')
