# Python 07. 객체 지향 프로그래밍

## 1. pip

\$ pip install faker

(1) faker 라는 파이썬 패키지를 설치하는 명령어

(2) cmd 창에서 실행

## 2. Basic Usages

```python
from faker import Faker  # 1 _faker 패키지에서 Faker 모듈을 사용_을 하기 위한 코드이다.

fake = Faker()  # 2 Faker는 _클래스_, fake는 _객체_이다.
fake.name()  # 3 name()은 fake의 _메서드_이다.
```

## 3. Localization

```python
class Faker():

    def __(a)__((b), (c)):
        pass
```

(a) init

(b) self

(c) language = 'en_US'

생성자 메서드를 구현하는 것이므로, 메서드 이름은 '\_\_init\_\_'이 되어야 하고, 메서드는 첫 번째 인자로 자기자신을 받으므로 self, 그리고 두 번째 인자로 어느나라의 언어인지를 받는데 default 값이 'en_US'이므로 (c)처럼 넣어줘야 합니다.

## 4. Seeding the Generator

(1) 

```python
fake1 = Faker(’ko_KR’)
Faker.seed(87654321)

print(fake1.name()) # 1

fake2 = Faker(’ko_KR’)
print(fake2.name()) # 2
```

\# 1 : 이진호 

\# 2 : 강은주

seed()는 난수값을 만들기 위한 시드값을 수동으로 설정해서 이 시드값으로 만들어진 다음 난수가 같도록(예측할수 있도록) 만드는 메서드인 것 같습니다.

(2)

```python
fake1 = Faker(’ko_KR’)
fake1.seed_instance(87654321)

print(fake1.name()) # 1

fake2 = Faker(’ko_KR’)
print(fake2.name()) # 2
```

\# 1 : 이진호

\# 2 : 김은정

seed_instance()도 seed()와 비슷한데 실행해보니깐 이 메서드가 인스턴스 메서드이고, 위의 seed()가 클래스 메서드인것 같습니다. 
