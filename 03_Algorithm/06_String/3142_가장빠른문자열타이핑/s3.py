#  이곳에 코드와 주석을 작성합니다.
#  가장 빠른 문자열 타이핑
#  s3.py
#  아직 실패

import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    a, b = input().split()

    cnt = 0  # a에 들어있는 b의 개수
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            cnt += 1
            i += len(b)
        else:
            cnt += 1
            i += 1
        if i + cnt*len(b) >= len(a):
            break

    print(f'#{t} {cnt}')