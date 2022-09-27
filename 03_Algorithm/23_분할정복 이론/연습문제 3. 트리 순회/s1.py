# 연습문제 3. 트리 순회


def preorder(v):
    if v:
        print(v, end=' ')
        preorder(ch1[v])
        preorder(ch2[v])


def inorder(v):
    if v:
        inorder(ch1[v])
        print(v, end=' ')
        inorder(ch2[v])


def postorder(v):
    if v:
        postorder(ch1[v])
        postorder(ch2[v])
        print(v, end=' ')


V, N = map(int, input().split())
edges = list(map(int, input().split()))

ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)

for i in range(0, 2 * N, 2):
    if ch1[edges[i]] == 0:
        ch1[edges[i]] = edges[i+1]
    else:
        ch2[edges[i]] = edges[i+1]

print('전위 순회 : ', end=' ')
preorder(1)
print()
print('중위 순회 : ', end=' ')
inorder(1)
print()
print('후위 순회 : ', end=' ')
postorder(1)
print()
