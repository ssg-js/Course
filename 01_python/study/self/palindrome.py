# 회문검사
T = int(input())

for test_case in range(1, T + 1):
    word = input()
    answer = 1
    for i, v in enumerate(word):
        if word[i] != word[-1 - i]:
            answer = 0
            break

    print(f'#{test_case} {answer}')
