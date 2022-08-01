# Python 06. 데이터 구조 및 활용

## 1. 무엇이 중복일까

```python
def duplicated_letters(word):
    letters = []  # 중복해서 나타난 문자들을 담는 list
    for digit in word:
        if (word.count(digit) >= 2) and not (digit in letters):
            # 중복이고 letters 리스트에 담기지 않는 문자일 경우
            letters.append(digit)
    return letters
```

## 2. 소대소대

```python
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
```

## 3. 솔로 천국 만들기

```python
def lonely(ls):
    new_ls = ls[:1]  # new_ls에 ls[0] 값 저장하고 시작
    for i in range(1, len(ls)):  # ls[0]이 아닌 ls[1]부터 시작
        if ls[i] == ls[i - 1]:  # 바로 앞의 숫자와 같은 경우
            continue
        else:  # 바로 앞의 숫자와 다른 경우 new_ls에 추가
            new_ls.append(ls[i])
    return new_ls
```


