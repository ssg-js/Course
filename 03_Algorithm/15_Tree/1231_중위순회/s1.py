# 1231_중위순회


def inorder(v):
    if v:
        inorder(ch1[v])
        answer.append(alpha[v])
        inorder(ch2[v])


for t in range(1, 11):
    num = int(input())
    infos = [input().split() for _ in range(num)]

    ch1 = [0] * (num + 1)  # 왼쪽 자식
    ch2 = [0] * (num + 1)  # 오른쪽 자식
    alpha = [''] * (num + 1)  # 각 인덱스에 해당하는 노드별 문자 정보
    answer = []

    for info in infos:
        parent = int(info[0])
        c = info[1]

        alpha[parent] = c
        if len(info) > 2:
            ch1[parent] = int(info[2])
            if len(info) == 4:
                ch2[parent] = int(info[3])

    inorder(1)

    print(f'#{t} ', end='')
    print(*answer, sep='')
