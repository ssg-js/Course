# 5189 전자카트


def moves(v, depth, usage):
    if depth == N:                              # N번까지 다 돌면
        usage += info[v][0]                     # 1번(0)으로 돌아가기
        usage_sum.append(usage)                 # 갔다 온 사용량 저장
        return

    for next_v in range(1, N):
        if not visited[next_v] and v != next_v:
            visited[next_v] = True              # 방문 여부 
            usage += info[v][next_v]            # 사용량 더해주기
            moves(next_v, depth + 1, usage)     # 재귀
            visited[next_v] = False             # 나오면 방문 여부 해제        
            usage -= info[v][next_v]            # 사용량도 원래대로


for t in range(1, int(input()) + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    usage_sum = []
    moves(0, 1, 0)

    print(f'#{t} {min(usage_sum)}')