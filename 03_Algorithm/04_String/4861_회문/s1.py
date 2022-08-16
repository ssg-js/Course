import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    words = [input() for _ in range(n)]

    answer = ''
    for i in range(n):
        for j in range(n-m+1):
            word = words[i]
            pldr = word[j:j+m]
            if pldr == pldr[-1:-len(pldr)-1:-1]:
                answer = pldr
                break
    else:
        for j in range(n):
            for i in range(n-m+1):
                pldr = ''
                for k in range(m):
                    pldr += words[i+k][j]
                if pldr == pldr[-1:-len(pldr)-1:-1]:
                    answer = pldr
                    break

    print(f'#{t} {answer}')