a = 1
if True:
    print(a + 1)


# import this

import math

num1 = 0.1 * 3
num2 = 0.3
print(math.isclose(num1, num2))

print(
    "\"파일은 c:\\Windows\\Users\\내문서\\Python\\에 저장이 되엇습니다.\"\n나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'"
)

name = '철수'
print('%s' % name)


print(458345 + 623576)

greeting = 'Hello'
month = 'july'

print(greeting + ' ' + month)


scores = [80, 89, 99, 83]
print(float(scores[0] + scores[1] + scores[2] + scores[3]) / 4)

lunch = {'돈까스': 9000, '써브웨이': 6000, '밥버거': 2500}
avg = (lunch['돈까스'] + lunch['써브웨이'] + lunch['밥버거']) / len(lunch)

print(avg)

n = 5
m = 9
print(('*' * n + '\n') * m)
