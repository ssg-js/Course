# 4366. 정식이의 은행업무


for t in range(1, 11):
    n = int(input())
    binary = input()            # 이진수 : 문자열!!!
    trinary = input()           # 3진수 : 문자열!!!!

    ans = 0
    for i, bi in enumerate(binary):
        temp_bi = (int(bi) + 1) % 2            # binary의 한자리가 틀린경우
        temp_binary = binary
        temp_binary = temp_binary[:i] + str(temp_bi) + temp_binary[i+1:]
        if int(temp_binary) == int(trinary):
            ans = int(temp_binary)
            break

        for j, tri in enumerate(trinary):       # trinary의 한자리기 틀린경우
            for plus in range(2):
                temp_tri = (int(tri) + plus) % 2
                temp_trinary = trinary
                temp_trinary = temp_trinary[:j] + str(temp_tri) + temp_trinary[j+1:]
                if int(binary) == int(temp_trinary):
                    ans = int(temp_binary)
                    break
            if ans:
                break
        if ans:
            break
    print(f'#{t} {ans}')
