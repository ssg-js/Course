import sys

sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t + 1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))

    # 정류장마다 충전기가 없으면 0, 있으면 1로 표시한 리스트 생성
    charge_stop = [0] * (n+1)
    for i in charge:
        charge_stop[i] = 1

    stop = 0  # 멈추는횟수
    start = 0  # 출발하는 위치

    while True:
        
        for i in range(k, -1, -1):  # 최대한의 거리부터 충전소있는지
            if (start + i) >= n:  # n 초과로 넘어가지 않도록
                break
            if charge_stop[start + i] == 1:  # 충전소가 있는위치일 경우
                stop += 1
                start += i
                break
            else:
                pass

        if (start + i) >= n:
            break
        elif i == 0:
            stop = 0
            break



    print(f'#{tc} {stop}')


