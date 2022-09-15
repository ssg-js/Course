#  연습문제 전위순회


def preorder(v):
    if v:
        answer.append(v)
        preorder(ch1[v])
        preorder(ch2[v])


num = int(input())
edges = list(map(int, input().split()))
answer = []

ch1 = [0] * (num + 1)  # 왼쪽 자식
ch2 = [0] * (num + 1)  # 오른쪽 자식

for i in range(0, len(edges), 2):
    a, b = edges[i], edges[i + 1]
    if ch1[a] == 0:
        ch1[a] = b
    else:
        ch2[a] = b

preorder(1)

print(*answer)
