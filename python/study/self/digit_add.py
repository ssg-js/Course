# 자릿수 더하기

number = int(input())

num_sum = 0
for i in range(number):
    num_sum += number % 10  # 일의 자릿수의 값을 더함
    number = number // 10  # 더한 일의 자릿수를 없앰

print(num_sum)
