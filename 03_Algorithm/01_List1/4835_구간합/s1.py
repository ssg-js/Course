import sys

sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    results = list()
    for i in range(n-m+1):
        num_sum = 0
        for j in range(m):
            num_sum += num[i+j]
        results.append((num_sum))

    for i in range(len(results)):
        for j in range(len(results) - i - 1):
            if results[j] > results[j+1]:
                results[j], results[j+1] = results[j+1], results[j]

    print(f'#{tc} {results[-1] - results[0]}')