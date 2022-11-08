# 4613. 러시아 국기 같은 깃발

# 위에서부터 흰색, 파란색, 빨강색 순으로 한줄 이상씩 있어야함

# idea
# N 줄의 국기를 만들고 원래 그림과 대조해서 최소값 구하기
# 인덱스 a, b 정하기 [:a], [a:b], [b:]
# 1 <= a < N - 1
# a < b < N

def combination(arr, start):
    if len(arr) == 2:
        ab.append(arr[:])
        return

    for i in range(start, N):
        arr.append(i)
        combination(arr, i + 1)
        arr.pop()


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    ab = []
    combination([], 1)

    change_cnt = []

    for case in ab:
        cnt = 0
        a, b = case
        part1 = board[:a]
        part2 = board[a:b]
        part3 = board[b:]
        for colors in part1:
            cnt += colors.count('B')
            cnt += colors.count('R')
        for colors in part2:
            cnt += colors.count('W')
            cnt += colors.count('R')
        for colors in part3:
            cnt += colors.count('W')
            cnt += colors.count('B')
        change_cnt.append(cnt)

    answer = min(change_cnt)

    print(f'#{t} {answer}')

