# 5201. 컨테이너 운반

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())                        # N: 화물, M: 트럭
    container_weight = list(map(int, input().split()))      # N개
    truck_power = list(map(int, input().split()))           # M개


