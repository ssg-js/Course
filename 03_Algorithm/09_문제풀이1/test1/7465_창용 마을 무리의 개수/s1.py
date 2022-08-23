import sys

sys.stdin = open('input.txt')


def dfs(x):
    counted[x] = True

    for person in relation[x]:
        if not counted[person]:
            dfs(person)


for t in range(1, int(input()) + 1):
    citizen, friends = map(int, input().split())

    relation = [[] for _ in range(citizen + 1)]
    counted = [False] * (citizen + 1)

    for i in range(friends):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)

    cnt = 0  # 무리의 개수
    for i in range(1, citizen + 1):
        if not counted[i]:
            dfs(i)
            cnt += 1

    print(f'#{t} {cnt}')

