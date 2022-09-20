# 5185. 이진수

hexadecimal = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',   # 10
    'B': '1011',   # 11
    'C': '1100',   # 12
    'D': '1101',   # 13
    'E': '1110',   # 14
    'F': '1111',   # 15
}

for t in range(1, int(input()) + 1):
    n, hexa = input().split()
    N = int(n)

    ans = ''
    for digit in hexa:
        ans = ans + hexadecimal[digit]

    print(f'#{t} {ans}')