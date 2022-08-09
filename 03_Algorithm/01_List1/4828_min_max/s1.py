import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    num = list(map(int, input().split()))

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

    sub_num = num[n-1] - num[0]
    print(f'#{tc} {sub_num}')
