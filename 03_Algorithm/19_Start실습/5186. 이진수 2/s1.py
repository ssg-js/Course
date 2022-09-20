# 5186. 이진수 2


for t in range(1, int(input()) + 1):
    N = float(input())

    i = 1
    last = N
    ans = ''
    while last != 0:
        if last - 2 ** (-1 * i) >= 0:
            last = last - 2 ** (-1 * i)
            ans = ans + '1'
        else:
            ans = ans + '0'
        if i > 12:
            ans = 'overflow'
            break
        i += 1

    print(f'#{t} {ans}')