import sys

sys.stdin = open('input.txt')

actions = input()

punch_cnt = [0, 0]

punches = actions.split('(^0^)')

for i in range(2):
    for move in punches[i]:
        if move == '@':
            punch_cnt[i] += 1

print(*punch_cnt)

# 매서드로 풀기
# left, right = input().split('0')
# print(left.count('@'), right.count('@')