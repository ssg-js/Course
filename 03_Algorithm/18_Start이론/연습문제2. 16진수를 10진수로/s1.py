# 연습문제 2 십육진수의 십진수 출력

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
    num = input()
    digits = ''
    for digit in num:
        digits = digits + hexadecimal[digit]

    binary = list(map(int, digits))
    ans = []
    n = 0
    for i in range(len(binary)):
        n = binary[i] + n * 2
        if i % 7 == 6:
            ans.append(n)
            n = 0
    ans.append(n)
    print(f'#{t}', *ans)

