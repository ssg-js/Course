# 회문2
# 가로, 세로 직선으로 가장 긴 회문 구하기

import sys

sys.stdin = open('input.txt')

for t in range(1, 10 + 1):
    n = int(input())
    grid = [input() for _ in range(100)]

    pldr = ''
    # 회문의 길이 m 정하기, 긴 길이부터 찾아서 길이 비교라도 덜하도록
    for m in range(100, 2, -1):
        for i in range(100):
            for j in range(100-m+1):
                # 가로 회문 찾기
                text = grid[i][j:j+m]
                if text == text[::-1]:
                    pldr = text
                # 세로 회문 찾기
                text = ''
                for k in range(m):
                    text = text + grid[j + k][i]
                if text == text[::-1]:
                    pldr = text
        if pldr:
            break

    print(f'#{t} {len(pldr)}')
