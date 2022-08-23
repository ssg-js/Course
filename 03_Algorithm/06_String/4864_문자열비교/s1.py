import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    str1 = input()
    str2 = input()

    match = 0
    for i in range(len(str2) - len(str1) + 1):
        if str2[i:i+len(str1)] == str1:
            match = 1
            break

    print(f'#{t} {match}')