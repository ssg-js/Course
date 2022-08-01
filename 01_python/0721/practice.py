'''
def ssafy(name, location = '서울'):
        print(f'{name}의 지역은 {location}입니다.')
# (1)
ssafy('가흔')
# (2)
ssafy(location='부울경', name='승현')
# (3)
ssafy('지우', location='서울')
# (4)
ssafy(name='승호', '광주')



##2
def my_avg(*args):
    sum = 0
    for n in args:
        sum += n

    return sum / len(args)


print(my_avg(77, 83, 95, 70, 80))



##3


def my_func(a, b):
    c = a + b
    print(c)


result = my_func(3, 7)
print(result)



# workshop

# 1


def measure(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')

        else:
            pass


measure(int(input("정수 입력하세요 ")))



# 2
def list_sum(l):
    hap = 0
    for i in l:
        hap += i

    return hap


print(list_sum([1, 2, 3, 4, 5]))



# 3
def dict_list_sum(l):
    hap = 0
    for i in range(0, len(l)):
        d = l[i]
        hap += d['age']

    return hap


print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]))



# 4
def all_list_sum(l):
    hap = 0
    for i in l:
        for j in i:
            hap += j

    return hap


print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))



# 5
def get_secret_word(l):
    word = ''
    for i in l:
        word += chr(i)

    return word


print(get_secret_word([83, 115, 65, 102, 89]))

# 6
def get_secret_number(word):
    order = {}
    hap = 0
    for i in list(map(ord, word)):
        hap += i

    return hap


# 7
def get_strong_word(a, b):
    a_sum = get_secret_number(a)
    b_sum = get_secret_number(b)

    if a_sum > b_sum:
        return a
    elif a_sum < b_sum:
        return b
    else:
        return a, b


print(get_strong_word('qwqwe', 'qwqwe'))
'''
# online_pratice
# 4-3
import random

ls = [random.randint(0, 9) for i in range(0, 7)]
print(ls)

for i, v in enumerate(ls):
    if i == 0:
        continue

    if v == ls[i - 1]:
        del ls[i]

print(ls)

complex
