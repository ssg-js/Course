import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    str1 = input()
    str2 = input()

    max_cnt = 0
    for a in str1:
        cnt = 0
        for b in str2:
            if b == a:
                cnt += 1
        if cnt >= max_cnt:
            max_cnt = cnt

    print(f'#{t} {max_cnt}')