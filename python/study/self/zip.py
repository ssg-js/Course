# 간단한 압축 풀기
# 성공

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    contents = []
    C = []
    K = []
    for i in range(N):
        f = input()
        contents = f.split()
        C.append(contents[0])
        K.append(int(contents[1]))

    count = 0  # 10개 출력시 다음 줄로 변경
    print(f'#{test_case}')
    for i, v in enumerate(K):
        for j in range(v):
            if count == 10:
                print()
                count = 0
            print(C[i], end='')
            count += 1
    print()
