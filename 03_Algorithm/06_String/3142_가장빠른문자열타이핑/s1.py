#가장 빠른 문자열 타이핑

import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    a, b = input().split()

    n = a.count(b)
    cnt = len(a) - n * len(b) + n
    print(f'#{t} {cnt}')