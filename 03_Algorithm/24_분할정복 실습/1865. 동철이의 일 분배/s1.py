# 1865 동철이
# 소수점 6번째까지 출력은 round(number, 6)
#
import sys
sys.stdin = open('input.txt')


def work_distribute(person, percentage):            # (1번 2번 3번 사람, 확률)
    global result
    for i in range(N):
        if not distributed[i]:                      # 아무도 안 한 일이면
            distributed[i] = True                   # 했다고 저장
            percent = percentage / 100 * efficiency[person - 1][i]
            if person == N:                         # 종료 조건 
                if percent * 100 > result:          # 비교하고 더 크면 
                    result = percent * 100          # 저장
                return                              # 돌아갓
            work_distribute(person + 1, percent)    # 다음 사람 일 맡기러 재귀
            distributed[i] = False                  #


for t in range(1, int(input()) + 1):
    N = int(input())
    efficiency = [list(map(float, input().split())) for _ in range(N)]
    distributed = [False] * N

    result = 0
    work_distribute(1, 1)

    print(f'#{t} {round(result, 6)}')







