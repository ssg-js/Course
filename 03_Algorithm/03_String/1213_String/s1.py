import sys

sys.stdin = open('test_input.txt', encoding='UTF8')

for t in range(1, 10 + 1):
    test_case = int(input())
    search = input()
    sentence = input()

    # 한방에
    # print(f'#{tc} {s.count(search)}')

    cnt = 0
    start = 0
    for index, cha in enumerate(sentence):
        for i, v in enumerate(search):
            if cha == search[start] and start == i:
                start += 1
                break
            elif i == len(search) - 1:
                start = 0

        if start == len(search):
            cnt += 1
            start = 0


    print(f'#{test_case} {cnt}')