# 배열 최소합
import sys

sys.stdin = open('input.txt')


def permutations(arr, n):
    if len(arr) == n:
        if sum(arr) == n:
            print(n)
        return

    if


for t in range(1, int(input()) + 1):
    length = int(input())
    array = [list(map(int, input())) for _ in range(length)]

    checked = [[False] * length for _ in range(length)]

    permutations([], length)



