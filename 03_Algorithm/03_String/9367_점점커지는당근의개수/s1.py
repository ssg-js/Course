import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    carrots = list(map(int, input().split()))

    max_seq = 1
    seq = 1
    for i in range(n - 1):
        if carrots[i] + 1 == carrots[i+1]:
            seq += 1
            if seq > max_seq:
                max_seq = seq
        else:
            seq = 1

    print(f'#{t} {max_seq}')