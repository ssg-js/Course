import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    pages, pa, pb = map(int, input().split())

    al, bl = 1, 1
    ar, br = pages, pages

    for _ in range(pages):
        # A
        ac = int((al + ar) / 2)
        if pa < ac:
            ar = ac
        elif pa > ac:
            al = ac
        elif pa == ac:
            ac = 0

        # B
        bc = int((bl + br) / 2)
        if pb < bc:
            br = bc
        elif pb > bc:
            bl = bc
        elif pb == bc:
            bc = 0

        result = ''
        if ac == 0 and bc == 0:
            result = '0'
            break
        elif ac == 0:
            result = 'A'
            break
        elif bc == 0:
            result = 'B'
            break
        else:
            pass

    print(f'#{t} {result}')
