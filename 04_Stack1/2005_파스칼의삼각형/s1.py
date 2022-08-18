import sys

sys.stdin = open('input.txt')


def pascal_tri(num):
    if num == 1:
        return [[1]]
    # 파스칼 삼각형이 들어있는 이차원 리스트
    tri = pascal_tri(num-1)
    # 새로운 줄을 담는 리스트
    li = [1 for _ in range(num)]
    for i in range(1, num-1):
        li[i] = tri[num-2][i-1] + tri[num-2][i]
    tri.append(li)
    # 만들어진 리스트를 원래 파스칼 삼각형에 추가
    return tri


for t in range(1, int(input()) + 1):
    n = int(input())
    print(f'#{t}')
    for line in pascal_tri(n):
        print(*line)



