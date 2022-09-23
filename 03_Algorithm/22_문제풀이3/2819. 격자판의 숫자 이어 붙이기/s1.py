# 격자판의 숫자 이어 붙이기
# 시작 - 14:54

# idea
# visited 안써도 됨
# 숫자는 str로 처리
# 임의의 자리에서 시작
# 6번 이동
# 이미 지났던 위치를 지날때 해당 자리를 지났을때 만들어진 숫자와 같으면 리턴...


def move(num):
    if len(num) == 8:            # 7자리 다 채우면
        if num not in numbers:
            numbers.append(num)
        return
    nx = i
    ny = j
    for di in range(4):          # 인접한 격자로 이동
        nx = nx + dx[di]
        ny = ny + dy[di]
        if 0 <= nx < 4 and 0 <= ny < 4:
            num = num + board[nx][ny]
            move(num)
            num = num[:-2]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for t in range(1, int(input()) + 1):
    board = [input().split() for _ in range(4)]
    numbers = []                # 각 숫자들 저장(중복x)
    info = [[] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            number = board[i][j]  # 시작숫자 저장
            move(number)

    cnt = len(numbers)
    print(f'#{t} {cnt}')


