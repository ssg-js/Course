# [BOJ] 7569. 토마토


M, N, H = map(int, input().split())

box = []
ripe = 1
for height in range(H):
    layer = []
    for i in range(N):
        line = list(map(int, input().split()))
        if ripe and 0 in line:
            ripe = 0
        layer.append(line)
    box.append(layer)

days = 0

if ripe == 0:
    while True:

