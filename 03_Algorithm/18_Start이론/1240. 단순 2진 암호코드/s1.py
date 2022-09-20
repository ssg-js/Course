# 1240 단순 2진 암호 코드

import sys
sys.stdin = open("input.txt")

pattern = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())        # N : 세로 크기, M : 가로 크기
    print(N, M)
    arr = [input() for _ in range(N)]
    codes = []                              # 8자리 코드를 저장

    for line in arr:                        # line이 0이 아니면
        i = 0
        while i < M - 7:
            code = line[i:i+7]
            if code in pattern.keys():
                codes.append(pattern[code])
                i += 6
            i += 1
    print(codes)
    cal = [0, 0]                            # 암호코드 검사할때 값을 저장
    for i in range(8):
        if i % 2 == 0:                      # 홀수 번째
            cal[0] += codes[i]
        else:
            cal[1] += codes[i]
    print(cal)
    ans = 0
    if (cal[0] * 3 + cal[1]) % 10 == 0:
        ans = cal[0] + cal[1]

    print(f'#{t} {ans}')

