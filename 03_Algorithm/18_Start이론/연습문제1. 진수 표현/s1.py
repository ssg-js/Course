# 진수 표현


for t in range(1, int(input()) + 1):
    binary = list(map(int, input()))

    ans = []
    n = 0
    for i in range(len(binary)):
        n = binary[i] + n * 2
        if (i % 7) == 6:
            ans.append(n)
            n = 0
    print(f'#{t}', *ans)
