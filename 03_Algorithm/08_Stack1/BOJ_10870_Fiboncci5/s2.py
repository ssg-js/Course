# fibonacci
# memoization

memo = [0, 1]


def fibo(n):
    if len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]


n = int(input())
print(fibo(n))