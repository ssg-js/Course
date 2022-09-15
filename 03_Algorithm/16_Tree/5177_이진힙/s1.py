# 5177 이진 힙


def heap_push(v):
    heap.append(v)
    child = len(heap) - 1
    parent = child // 2

    while parent > 0 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


for t in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    heap = [0]
    for number in numbers:
        heap_push(number)

    child = len(heap) - 1       # 마지막 노드
    parent = child // 2         # 조상 노드
    nodes_sum = 0
    while parent > 0:
        nodes_sum += heap[parent]
        child = parent
        parent = child // 2

    print(f'#{t} {nodes_sum}')

