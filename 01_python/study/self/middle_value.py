# 중간값 찾기
# 성공

N = int(input())

input_number = input().split()
numbers = list(map(int, input_number))  # 각 숫자를 정수형을 변환
numbers.sort()  # 순서대로 정렬

print(numbers[N // 2])
