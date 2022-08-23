# import random
import sys

sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    space = list()

    # 랜덤값으로 리스트 알아서 만들면
    # n = 5
    # for i in range(n):
    #     li = []
    #     for j in range(n):
    #         li.append(random.randrange(1, 25))
    #
    #     space.append(li)

    # 입력으로 n과 이차원리스트 받기
    n = int(input())
    for i in range(n):
        li = list(map(int, input().split()))
        space.append((li))

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    sub_sum = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if (0<=ni<n) and (0<=nj<n):
                    if space[ni][nj] > space[i][j]:
                        sub_sum += (space[ni][nj] - space[i][j])
                    else:
                        sub_sum += (space[i][j] - space[ni][nj])

    print(f'#{tc} {sub_sum}')