import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    students, submit = map(int, input().split())

    submit_students = list(map(int, input().split()))

    no_submit = []

    for i in range(1, students + 1):
        if i not in submit_students:
            no_submit.append(i)

    no_submit.sort()

    print(f'#{t}', *no_submit)