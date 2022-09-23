# 4366. 정식이의 은행업무


def decimal(arr, k):                       # k진수를 10진수로
    result = 0
    for index in range(len(arr)):
        result += (k ** index) * arr.pop()
    return result


for t in range(1, int(input()) + 1):
    binary = list(map(int, input()))
    trinary = list(map(int, input()))

    ans = 0
    for i, bi in enumerate(binary):
        temp_bi = (bi + 1) % 2             # binary의 한자리 바꾸기
        temp_binary = binary[:]
        temp_binary[i] = temp_bi           # 틀린 자리 수정
        b = decimal(temp_binary[:], 2)

        for j, tri in enumerate(trinary):  # trinary의 한자리 바꾸기
            for plus in range(1, 3):
                temp_tri = (tri + plus) % 3
                temp_trinary = trinary[:]
                temp_trinary[j] = temp_tri
                a = decimal(temp_trinary[:], 3)
                if a == b:  # 3진수와 일치하면 정답
                    ans = a
                    break
            if ans:
                break
        if ans:
            break
    print(f'#{t} {ans}')
