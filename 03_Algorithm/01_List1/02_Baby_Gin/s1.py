import sys

sys.stdin = open("input.txt")



T = int(input())

for test_case in range(1, T + 1):
    # 띄어쓰기 없는 스트링을 쪼개서 정수인 리스트를 만들기
    cards = input()[:]
    cards = list(map(int, cards))
    counter = [0 for i in range(12)]  # row를 판별할 때 오류가 안나기 위해서 10개 + 2개
        
    # 숫자별 개수 세기
    for i, v in enumerate(cards):
        counter[v] += 1

    triplet = 0
    row = 0
    for i, v in enumerate(cards):
        if counter[i] == 3:
            counter[i] -= 3
            triplet += 1
            continue

        if counter[i] == 1 and counter[i+1] == 1 and counter[i+2] == 1:
            counter[i] -= 1
            counter[i + 1] -= 1
            counter[i + 2] -= 1
            row += 1

    baby_gin = 0  # baby_gin 일 경우 1
    if triplet + row == 2:
        baby_gin = 1
    print(cards)
    print(f'#{test_case} {baby_gin}')




