#  이곳에 코드와 주석을 작성합니다.
#  가장 빠른 문자열 타이핑
#  s2.py

import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    a, b = input().split()

    n = 0  # a에 들어있는 b의 개수
    i = 0

    while i <= len(a)-len(b):
        # b일때
        if a[i:i+len(b)] == b:
            n += 1
            i += len(b)
        # b가 아닌 다른 문자일때
        else:
            i += 1

    cnt = len(a) - n * len(b) + n
    print(f'#{t} {cnt}')