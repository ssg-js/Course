import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    # 색칠 정보(박스)의 개수
    num_box = int(input())

    grid = [[0] * 10 for _ in range(10)]
    purple_area = 0

    # 색칠 정보 받아서 개수만큼 칠하기
    for _ in range(num_box):
        info = list(map(int, input().split()))

        start = info[0:2]
        end = info[2:4]
        color = info[4]
        x = 1 if end[0] - start[0] > 0 else -1
        y = 1 if end[1] - start[1] > 0 else -1

        # 가로
        for i in range(start[0], end[0] + x, x):
            # 세로
            for j in range(start[1], end[1] + y, y):
                # 색칠되어있는 색과 같은 경우 그대로
                if grid[i][j] == color:
                    grid[i][j] = color
                # 색칠되어있는 색과 다른 경우 더하기(purple은 3이상)
                else: 
                    grid[i][j] += color

    for i in range(10):
        for j in range(10):
            if grid[i][j] >= 3:
                purple_area += 1

    print(f'#{t} {purple_area}')

