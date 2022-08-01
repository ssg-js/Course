# Python 03. 제어문과 함수

## 1. Built-in 함수

print(), input(), split(), sort(), int(), str(), set()

## 2. 홀수만 담기

```python
ls = [i for i in range(1, 50)]
ls = ls[::2]
```

## 3. 반복문으로 네모 출력

```python
for i in range(0, m):
    print('*' * n)
```

## 4. 조건 표현식

```python
print('입실 불가') if temp >= 37.5 else print('입실 가능')
```

## 5. 정중앙 문자

```python
def get_middle_char(args):
    l = int(len(args))
    print(type(args))
    if l % 2 == 0:
        r = args[int(l/2 - 1):int(l/2 + 1)]
    else:
        r = args[int((l-1)/2)]
    return r
```


