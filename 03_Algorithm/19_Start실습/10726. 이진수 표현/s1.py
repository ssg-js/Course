# 10726. 이진수 표현


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    binary = bin(M)
    status = 'ON'
    i = 1
    while i < len(binary):
        if binary[-i] != '1':       # binary는 문자열 타입!!!!
            status = 'OFF'
            break
        if i == N:
            break
        i += 1
    if i != N:
        status = 'OFF'

    print(f'#{t} {status}')