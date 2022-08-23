import sys

sys.stdin = open('input.txt')


for t in range(1, int(input()) + 1):
    num = int(input())
    cards = input().split()
    
    # 절반으로 나눌 덱, 왼쪽 덱이 교대로 놓을때 먼저 놓는 덱
    left_cards = []
    right_cards = []
    for i, n in enumerate(cards):
        if i < num / 2:
            left_cards.append(n)
        else:
            right_cards.append(n)

    shuffle = []
    for i in range(num):
        if i % 2 == 0:
            shuffle.append(left_cards[i//2])
        else:
            shuffle.append(right_cards[i//2])

    print(f'#{t}', *shuffle)
