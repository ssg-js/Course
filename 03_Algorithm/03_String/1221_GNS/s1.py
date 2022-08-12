import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    test_case, n = input().split()
    num_str = input().split()

    num_sys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    arr = ''
    for num in num_sys:
        for i in range(num_str.count(num)):
            arr += num + ' '

    print(f'{test_case}')
    print(f'{arr}')
