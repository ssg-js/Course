import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    li = list(map(int, input().split()))

    for cnt in range(n):
        for i in range(1, n-cnt):
            if cnt % 2 == 0:
                if li[-i] > li[-1-i]:
                    li[-i], li[-1-i] = li[-1-i], li[-i]
            else:
                if li[-i] < li[-1-i]:
                    li[-i], li[-1-i] = li[-1-i], li[-i]

    # 언패킹을 통해 나열
    li = li[0:10]
    print(f'#{t}', *li)
