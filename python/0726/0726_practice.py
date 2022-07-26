# homework
# 1
from black import Changed


ls = [3, 6, 5, 7, 7, 4, 7, 2]
print(ls.sort())
# None
print('---------')
print(ls)
# [2, 3, 4, 5, 6, 7, 7, 7]
print('---------')
ls = [3, 6, 5, 7, 7, 4, 7, 2]
print(sorted(ls))
# [2, 3, 4, 5, 6, 7, 7, 7]


# 2
x = ['hello', 'python']
y = ['hello', 'java']
x.append(y)
print(x)
# ['hello', 'python', ['hello', 'java']]
x = ['hello', 'python']
y = ['hello', 'java']
x.extend(y)
print(x)
# ['hello', 'python', 'hello', 'java']


# workshop
# 1
def duplicated_letters(word):
    letters = []  # 중복해서 나타난 문자들을 담는 list
    for digit in word:
        if (word.count(digit) >= 2) and not (digit in letters):
            # 중복이고 letters 리스트에 담기지 않는 문자일 경우
            letters.append(digit)
    return letters


print(duplicated_letters('apple'))
print(duplicated_letters('banana'))


# 2
def low_and_up(word):
    changed = ''
    num = 1
    for digit in word:
        if (num % 2 == 1) and (digit.isupper()):
            # 홀수번째 문자가 대문자인 경우
            changed += chr(ord(digit) + (ord('a') - ord('A')))
        elif (num % 2 == 0) and (digit.islower()):
            # 짝수번째 문자가 소문자인 경우
            changed += chr(ord(digit) + (ord('A') - ord('a')))
        else:  # 바꾸지 않아도 되는 경우
            changed += digit
        num += 1
    return changed


print(low_and_up('apple'))
print(low_and_up('banana'))


# 3
def lonely(ls):
    new_ls = ls[:1]  # new_ls에 ls[0] 값 저장하고 시작
    for i in range(1, len(ls)):  # ls[0]이 아닌 ls[1]부터 시작
        if ls[i] == ls[i - 1]:  # 바로 앞의 숫자와 같은 경우
            continue
        else:  # 바로 앞의 숫자와 다른 경우 new_ls에 추가
            new_ls.append(ls[i])
    return new_ls


print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))


# online_practice
salty_water = []
for i in range(5):
    salty_water.append(input(f"{i+1}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:"))
    stop = input("Done 입력 시 농도와 양 출력")
    if stop == 'Done':
        salt = 0
        water = 0
        for source in salty_water:
            divide = source.split()  # divde[0] = 'xx%', divide[1] = 'xxxg'
            salt += int((divide[0])[:-1]) * (int((divide[1])[:-1]) / 100)
            # [:-1]은 뒤에 붙은 %와 g을 없애는 작업
            # 농도 * 소금물 / 100 = 소금양
            water += int((divide[1])[:-1])

        print(f"{round((salt / water * 100), 2)}% {water}g")
        break
