# 4366. 정식이의 은행업무


def decimal(arr, k):                       # k진수를 10진수로
    result = 0
    for index in range(len(arr)):
        result += (k ** index) * arr.pop()
    return result


for t in range(1, 11):
    n = int(input())
    binary = list(map(int, input()))
    trinary = list(map(int, input()))

    ans = 0
    for i, bi in enumerate(binary):
        temp_bi = (bi + 1) % 2             # binary의 한자리가 틀린경우
        temp_binary = binary[:]
        temp_binary[i] = temp_bi            # 틀린 자리 수정

        for j, tri in enumerate(trinary):  # trinary의 한자리가 틀린경우
            for plus in range(2):
                temp_tri = (int(tri) + plus) % 2
                temp_trinary = trinary[:]
                temp_trinary[j] = temp_tri
                if decimal(temp_trinary[:], 3) == decimal(temp_binary[:], 2):  # 3진수와 일치하면 정답
                    ans = decimal(temp_trinary[:], 3)
                    break
            if ans:
                break
        if ans:
            break
    print(f'#{t} {ans}')
