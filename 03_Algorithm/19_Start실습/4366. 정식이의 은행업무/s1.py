# 4366. 정식이의 은행업무


def decimal(arr, k):                       # k진수를 10진수로
    result = 0
    for index in range(len(arr)):
        result += k ** arr.pop()


for t in range(1, 11):
    n = int(input())
    binary = list(map(int, input()))
    trinary = list(map(int, input()))

    ans = 0
    for i, bi in enumerate(binary):
        temp_bi = (bi + 1) % 2             # binary의 한자리가 틀린경우
        temp_binary = binary[:]
        temp_binary[i] = temp_bi
        if temp_binary == int(trinary):
            ans = temp_binary
            break

        for j, tri in enumerate(trinary):  # trinary의 한자리가 틀린경우
            for plus in range(2):
                temp_tri = (int(tri) + plus) % 2
                temp_trinary = int(trinary, 3)
                digit = temp_trinary
                temp_trinary += 3 * (bi_digit_num - j)
                if int(binary) == int(temp_trinary):
                    ans = int(temp_binary)
                    break
            if ans:
                break
        if ans:
            break
    print(f'#{t} {ans}')
