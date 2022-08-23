import sys

sys.stdin = open('test_input.txt', encoding='UTF8')

for t in range(1, 10+1):
    test_case = int(input())
    search = input()
    sentence = input()

    # 한방에
    print(f'#{tc} {s.count(search)}')

