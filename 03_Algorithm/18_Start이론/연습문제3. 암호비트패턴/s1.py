# 암호 비트 패턴

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

password_bit_patterns = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}


for t in range(1, int(input()) + 1):
    digits = input()
    number = ''
    for digit in digits:
        number = number + hexadecimal[digit]

    ans = []
    i = 0
    while i < len(number) - 6:
        pattern = number[i:i+6]
        if pattern in password_bit_patterns.keys():
            ans.append(password_bit_patterns[pattern])
            i += 5
        i += 1

    print(f'#{t}', *ans)




