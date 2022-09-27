# 5208. 전기 버스 2 (백트래킹)
# 1개당 0.2초 2천만연산
# N <= 100, M < N


def battery_change(battery, cnt, bus_stop):     # (남은배터리, 교체횟수, 현재 정류장)
    global min_cnt
    if cnt > min_cnt:                           # 가지치기
        return
    # if battery < 0:                           # 안 일어날 듯
    #     return
    for i in range(battery, 0, -1):             # 남은 배터리로 갈 수 있는 경우
        if bus_stop + i == N:                   # 도착하는 경우
            min_cnt = cnt
            return
        if bus_stop + i < N:                    # 최대 N번 정류장
            battery_change(bus_stop_battery[bus_stop + i - 1], cnt + 1, bus_stop + i)


for t in range(1, int(input()) + 1):
    info = list(map(int, input().split()))
    N = info[0]                                 
    bus_stop_battery = info[1:N]                # N-1 정류장까지 배터리정보

    min_cnt = N

    battery_change(bus_stop_battery[0], 0, 1)

    print(f'#{t} {min_cnt}')
    