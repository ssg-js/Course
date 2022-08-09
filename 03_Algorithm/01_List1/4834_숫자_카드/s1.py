import sys

sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1, t + 1):
    num = int(input())
    cards = list(map(int, input()[:]))

    counter = [0 for i in range(10)]
    # 각 인덱스에 해당하는 숫자별 개수를 값으로 가지는 list
    for i, v in enumerate(cards):
        counter[v] += 1

    max_index = 0
    max_value = 0
    for i, v in enumerate(counter):
        if v >= max_value:
            max_index = i
            max_value = v
    print(f'#{tc} {max_index} {max_value}')

