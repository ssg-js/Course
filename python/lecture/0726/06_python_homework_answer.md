# Python 06. 데이터  구조 및 활용

## 1. Built-in 함수와 메서드

```python
ls = [3, 6, 5, 7, 7, 4, 7, 2]
print(ls.sort())
# None
print('---------')
print(ls)
# [2, 3, 4, 5, 6, 7, 7, 7]
print('---------')
ls = [3, 6, 5, 7, 7, 4, 7, 2]
print(sorted(ls))
# [2, 3, 4, 5, 6, 7, 7, 7]d(ls))
```

sort()는 기존 리스트를 정렬하는 함수로 return 이 None입니다.

sorted()는 정렬된 새로운 리스트를 반환하는 함수입니다.

## 2. .extend()와 .append()

```python
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
```

x.append(y)는 리스트 x 끝에 y를 통째로 넣고

x.extend(y)는 리스트 x 끝에 y의 모든 항목을 넣습니다.

## 3. 복사가 잘 된 건가?

```python
a = [1, 2, 3, 4, 5]
b = a
a[2] = 5
print(a)
print(b)
```

둘 다 똑같이 [1, 2, 5, 4, 5]가 출력이 된다. 왜냐하면 b에 a가 가르키는 주소를 할당했기 때문이다.
