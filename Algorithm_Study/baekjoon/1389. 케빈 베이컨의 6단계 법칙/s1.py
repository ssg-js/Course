# [BOJ] 1389. 케빈 베이컨의 6단계 법칙

N, M = map(int, input().split())

rel = []                    # 친구 관계 저장
kb_num = [0] * N            # 해당 유저의 케빈베이컨 수 저장

for i in range(M):
    a, b = map(int, input().split())
    rel.append([a, b])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j != i:
            while True:
                