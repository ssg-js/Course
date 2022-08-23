import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    arr = input()

    max_seq = 0
    seq = 0
    for i in range(len(arr)):
        if arr[i] == '1':
            seq += 1
            if seq > max_seq:
                max_seq = seq
        else:
            seq = 0

    print(f'#{t} {max_seq}')