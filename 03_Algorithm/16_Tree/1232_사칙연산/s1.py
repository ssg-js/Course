# 1232 사칙연산


def postorder_cal(v):
    if v:
        postorder_cal(ch1[v])
        postorder_cal(ch2[v])
        if values[v] == '-':
            values[v] = str(int(values[ch1[v]]) - int(values[ch2[v]]))
        elif values[v] == '+':
            values[v] = str(int(values[ch1[v]]) + int(values[ch2[v]]))
        elif values[v] == '*':
            values[v] = str(int(values[ch1[v]]) * int(values[ch2[v]]))
        elif values[v] == '/':
            values[v] = str(int(values[ch1[v]]) // int(values[ch2[v]]))


for t in range(1, 11):
    N = int(input())

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    
    values = [''] * (N + 1)          # 각 노드에 들어가있는 정보

    for _ in range(N):
        info = input().split()
        parent = int(info[0])
        values[parent] = info[1]
        if not info[1].isdigit():   # 숫자가 아닌 사칙연산이면
            ch1[parent] = int(info[2])
            ch2[parent] = int(info[3])

    postorder_cal(1)
    print(f'#{t} {values[1]}')
