import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    words = [input() for _ in range(5)]

    n = len(words)
    m = 0
    # 가로 최대길이 구하기
    for i, v in enumerate(words):
        if len(v) > m:
            m = len(v)
    text = ''
    for j in range(m):
        for i in range(n):
            # 글자가 있는 경우
            if words[i][j]:
                text = text + words[i][j]
            # 글자가 없는 경우
            else:
                continue
