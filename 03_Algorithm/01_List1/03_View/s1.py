import sys

sys.stdin = open('input.txt')


for tc in range(1, 11):
    n = int(input())

    buildings = list(map(int, input().split()))

    good_home = 0

    for i, building in enumerate(buildings):
        for floor in range(building, 0, -1):  # 제일 위층 부터 count
            if (floor > buildings[i-2]) and (floor > buildings[i-1]) and (floor > buildings[i+1]) and (floor > buildings[i+2]):
                good_home += 1

    print(f'#{tc} {good_home}')
