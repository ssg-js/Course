# Python 03. 제어문

## 1. 세로로 출력하기

```python
n = int(input('자연수를 입력하세요'))
for i in range(1,n+1):
    print(i)
```

## 2. 가로로 출력하기

```python
n = int(input('자연수를 입력하세요'))
for i in range(1,n+1):
    print(i, end=' ')
```

## 3. 거꾸로 세로로 출력하기

```python
n = int(input('자연수를 입력하세요'))
while n >= 0:
    print(n)
    n -= 1
```

## 4. 거꾸로 출력해 보아요

```python
n = int(input('자연수를 입력하세요 '))
while n >= 0:
    print(n, end=' ')
    n -= 1
```

## 5. N줄 덧셈

```python
sum = 0
n = int(input('자연수를 입력하세요 '))
for i in range(1,n+1):
    sum += i
print(sum)
```

## 6. 삼각형 출력하기

```python
n = int(input('자연수를 입력하세요 '))
for i in range(1,n+1):
    print(' '*(n-i), end='')
    print('*'*i)
```

## 7. 중간값 찾기

```python
numbers.sort()
l = len(numbers)
if l % 2 == 1:
    print(numbers[int((l - 1) / 2)])
else:
    print(int(numbers[l / 2] + numbers[l / 2 - 1]))
```
