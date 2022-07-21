# Python : 제어문 및 함수

## 제어문 - 조건문, 반복문

- 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행

- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함

- 제어문은 순서도(flowchart)로 표현이 가능

### 조건문

#### 조건문

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

#### 기본 형식

- 조건에는 참/거짓에 대한 조건식(들여쓰기 주의!!)

```python
if 조건 == True:
    #Run this Code block
else :
    #Run this Code block
```

#### 조건문 실습 문제

- 조건문을 통해 변수 num값의 홀수/짝수 여부를 출력하시오. 이때 num은 input을 통해 사용자롭터 입력을 받으시오

```python
num = int(input('숫자 입력'))
if num % 2 == 1 :
    print('odd')
else :
    print('even')
```

#### 복수 조건문

- 복수의 조건식을 활용할 경우 elif를 활용하여 표현함

#### 복수 조건문 실습 문제

- 미세먼지 농도에 따른 위험 등급이 다음과 같을 때, dust 값에 따라 등급을 출력하는 조건식을 작성하시오.
  
  좋음(0<dust<=30), 보통(30<dust<=80), 나쁨(80<dust<=150), 매우나쁨(150<dust)
  
  ```python
  dust = 80
  if dust > 150: 
      print("매우나쁨")
  elif dust > 80:
      print("나쁨")
  elif dust > 30:
      print("보통")
  else: 
      print("좋음")
  print("미세먼지 확인 완)
  ```

#### 중첩 조건문

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음
  
  - 들여쓰기에 유의하여 작성할 것

### 조건 표현식

#### 조건 표현식

- 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용

- 삼항 연산자(Temary Operator)로 부르기도 함
  
  ```python
  true인 경우 값 if 조건 else false인 경우 값
  ```

#### 조건 표현식 실습 문제

```python
num = 2
if num % 2 :
    result = '홀수입니다'
else:
    result = '짝수입니다'
print(result)
```

삼항연산자로 바꾸면

```python
num = 2
result = '홀수입니다' if num % 2 else '짝수입니다'
```

### 반복문

#### 반복문

- 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용

#### 반복문의 종류

- while 문
  
  - 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함

- for 문
  
  - 반복가능한 객체를 모두 순회하면 종료(별도의 종료조건 불필요)

- 반복 제어
  
  - break, continue, for-else

#### while 문

- 조건식이 참인 경우 "들여쓰기가 되어 있는" 코드블록을 실행하고 다시 조건식이 참인지 확인

- while 문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요

```python
while 조건:
    # Code block
```

#### while 문 예시

```python
a = 0
while a < 5:  #종료 조건
    print(a)
    a += 1    #반복시 a가 계속 증가
print('end')
```

#### 복합 연산자(In-Place Operator)

- 복합 연산자는 연산과 할당을 합쳐 놓은 것

```python
a = 0         #a가 복합 연산자 
while a < 5:  #종료 조건
    print(a)
    a += 1    #반복시 a가 계속 증가
print('end')
```

### for 문

#### for 문

- for 문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소를 모두 순회
  
  - 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 불필요

- Iterable
  
  - 순회할 수 있는 자료형(string, list, dict, tuple, range, set 등)
  
  - 순회형 함수(range, enumerate)
  
  ```python
  for 변수명 in iterable:
      # Code block
  ```

#### for 문을 이용한 문자열(String) 순회

- 사용가 입력한 문자를 한 글자씩 출력하시오.

```python
chars = input()

for char in chars:
    print(char)
```

- range 사용

```python
chars = input()

for idx in range(len(chars)):
    print(chars[idx])
```

#### 딕셔너리(Dictionary) 순회

- 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

```python
grades = {'john' : 80, 'eric' : 90}
for student in grades:
    print(student)
'''실행결과
john
eric
'''
for student in grades:
    print(student, grades([student])
'''실행결과
john 80
eric 90
'''
```

#### 추가 메서드를 활용한 딕셔너리 순회

- 추가 메서드를 활용하여 순회할 수 있음
  
  - keys() : Key로 구성된 결과
  
  - value() : value로 구성된 결과
  
  - item() : (Key, value)의 튜플로 구성되 결과

```python
grades = {'john' : 80, 'eric' = 90}
for student, grade in grades.items():
    print(student, grade)
'''실행결과
john 80
eric 90
'''
```

#### enumerate 순회

- enumerate() : (index, value) 형태의 tuple로 구성된 열거 객체를 반환

```python
member = ['민수', '영희', '철수']
for idx, number in enumerate(members):
    print(idx, number)
'''
0 민수
1 영희
2 철수
'''
```

- 파이썬 문서에서 확인하기
  
  - enumerate(iterable, start=0)

#### List Comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
  
  ```python
  [code for 변수 in iterable]
  [code for 변수 in iterable if 조건식]
  ```

#### Dictionary Comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
  
  ```python
  {key: value for 변수 in iterable}
  {key: value for 변수 in iterable if 조건식}
  ```

### 반복문 제어

#### 반복문 제어

- break : 반복문을 종료

- continue : continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수해

- for-else : 끝까지 반복문을 실행한 이후에 else문 실행
  
  - break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음

- pass : 아무것도 하지 않음(문법적으로 필요하지만, 할 일이 없을 때 사용)

### 함수

#### 개요

- 함수 기초

- 함수의 결과값(Output)

- 함수의 입력(Input)

- 함수의 범위(Scope)

- 함수의 문서화(Doc-string)

- 함수 응용

#### 함수

- 함수를 사용하는 이유
  
  - Decomposition(분해) : 기능을 분해하고 재사용 가능하게 만드는 것
  
  - Abstraction(추상화) : 복잡한 내용을 모르더라고 사용할 수 있도록(블랙박스)하고 재사용성과 가독성, 생산성을 높이는 것

### 함수 기초

#### 함수의 종류

- 함수는 크게 3가지로 분류
  
  - 내장 함수 : 파이썬에 기본적으로 포함된 함수
  
  - 외장 함수 : import 문을 통해 사용하며, 외부 라이브러리에서 제공되는 함수
  
  - 사용자 정의 함수 : 직접 사용자가 만드는 함수

#### 함수의 정의

- 함수(Function)
  
  - 특정한 기능을 하는 코드의 조각(묶음)
  
  - 특정 코드를 매번 다시 작성하기 않고, 필요 시에만 호출하여 간편히 사용

#### 함수 기본 구조

- 선언과 호출(define & call)

- 입력(input)

- 문서화(Doc-String)

- 범위(Scope)

- 결과값(Output)

#### 선언과 호출(define & call)

- 함수의 선언은 def 키워드를 활용

- 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함
  
  - Docstring은 함수 body 앞에 선택적으로 작성 가능
  
  - 작성시에는 반드시 첫 번째 문장에 문자열 ''''''

- 함수는 parameter를 넘겨줄 수 있음

- 함수는 동작 후에 return을 통해 결과값을 전달함

#### 함수의 정의

```python
def function_name(parameter):
    # code block
    return returning_value
```

#### 선언과 호출(define & call)

- 함수는 함수명()으로 호출하여 사용
  
  - parameter가 있는 경우, 함수명(값1, 값2, ...) 로 호출

```python
def add(x, y):
    return x + y

add(2,3)
```

### 함수의 결과값

#### 값에 따른 함수의 종류

- Void function
  
  - 명시적인 return 값이 없는 경우, None을 반환하고 종료

- Value returning function
  
  - 함수 실행 후, return문을 통해 값 반환
  
  - return을 하게 되면, 값 반환 후 함수가 바로 종료
    
    - print는 값을 출력하지만 값을 반환하진 않음
    
    - REPL(Read-Eval-Print Loop) 환경에서는 마지막으로 작성된 코드의 리턴 값을 보여주무로 같은 동작을 하는 것으로 착각할 수도 있음(jupyter notebook)

#### 두개 이상의 값 반환

- 반환 값으로 튜플 사용

```python
def minus_and_product(x, y):
    return x - y, x + y
y = minus_and_product(4, 5)
print(y)    # (-1, 20)
print(type(y))    # <class 'tuple'>
```

- 리스트와 캍은 컨테이너를 활용하여 return 가능

### 함수 입력

#### Parameter와 Argument

- Parameter : 함수를 정의할 때, 함수 내부에서 사용되는 변수

- Argument : 함수를 호출 할 때, 넣어주는 값
  
  ```python
  def function(ham):    # parameter : ham
      # ...
  function('spam')    # argument : 'spam'
  ```

#### Argument

- Argument : 함수 호출 시 함수의 parameter를 통해 전달되는 값
  
  - 필수 Argument : 반드시 전달되어야 하는 argument
  
  - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본값이 전달

#### Positional Arguments

- 기본적으로 함수 호출 수 Argument는 위치에 따라 함수 내에 전달됨

#### Keyword Arguments

- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음

- Keyword Argument 다음에 Positional Argument를 활용할 수 없음

```python
def add(x, y):
    return x + y
add(x = 2, y = 5)
add(2, y = 5)
add(x = 2, 5) -> Error
```

#### Default Arguments Values

- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
  
  ```python
  def add(x, y = 0):
      return x + y
  add(2)     # x = 2, y = 0, 2
  ```

#### 정해지지 않은 여러 개의 Arguments 처리

print 함수의 Argument 개수가 변해도 잘 동작하는 이유는?

```python
print('you', 'need', 'python')
```

애스터리스크(Asterisk) 혹은 언패킹 연산자라고 불리는 * 덕분

#### 가변 인자(\*args\*)

- 가변 인자란?
  
  - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용

- 언제 사용하는가? 
  
  - 몇 개의 Positional Argument를 받을 지 모르는 함수를 정의할 때 유용

#### 패킹 / 언패킹

- 가변 인자를 이해하기 위해서는 패킹, 언패킹을 이해해야 함

- 패킹 : 여러 개의 데이터를 묶어서 변수에 할당하는 것

```python
numbers = (1, 2, 3)    # 패킹
```

- 언패킹 : 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것

```python
numbers = (1, 2, 3)
a, b, c = numbers    #언패킹
```

- 언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야함

- 언패킹시 왼쪽의 변수에 asterisk(*)를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음

```python
numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers    # 1, 2를 제외한 나머지를 rest에 대입
a, *rest, e = numbers    # 1, 5를 제외한 나머지를 rest에 대입     
```

#### Asterisk(\*)와 가변 인자

- \*는 시퀀스 언패킹 연산자라도 부리며, 말 그대로 시퀀스를 풀어 헤치는 연산자
  
  - 주로 튜플이나 리스트를 언패킹하는데 사용
  
  - \*를 활용하여 가변 인자를 만들 수 있음

#### 가변 키워드 인자(\*\*kwargs)

- 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용

- \*\*kwargs는 **딕셔너리**로 묶여 처리되며, parameter에 \*\*를 붙여 표현

```python
def family(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
family(father = '아부지', mother = '어무니', baby = '아기')
```



### Python의 범위(Scope)

#### Python의 범위(Scope)

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

- scope
  
  - glabal scope : 코드 어디에서든 참조할 수 있는 공간
  
  - local scope : 함수가 만든 scope, 함수 내부에서만 참조 가능

- variable
  
  - global variable : global scope에 정의된 변수
  
  - local variable : local scope에 정의된 변수

#### 변수 수명주기(lifecycle)

- 변수는 각자의 수명주기(lifecycle)가 존재
  
  - built-in scope : 파이썬이 실행된 이후부터 영원히 유지
  
  - global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  
  - local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

#### 이름 검색 규칙(Name Resolution)

- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음

- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
  
  - Local scope : 지역 범위(현재 작업 중인 범위)
  
  - Enclosed scope : 지역 범위 한 단계 위 범위
  
  - Global scope : 최상단에 위치한 범위
  
  - Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것) ex) print()

#### global 문

- 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global varible임을 나타냄
  
  - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
  
  - global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함

#### global 관련 에러

```python
a = 10
def func1():
    print(a)    # error : global a 선언 전에 사용
    global a
```

```python
a = 10
def func1(a):    
    global a    # error : parameter에 global 사용 불가
```

#### nonlocal

- global을 제외하고 가장 가까운(둘러싸고 있는) scope의 변수를 연결하도록함
  
  - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
  
  - nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함

- global과는 달리 이미 존재하는 이름과의 연결만 가능함

#### 함수의 범위 주의

- 기본적은 함수에는 선언된 변수는 local scope에 생성되며, 함수 종료 시 사라짐

- 함수 내에서 필요한  상위 scope 변수는 argument로 넘겨서 활용할 것

- glabal, nonlocal 키워드의 경우 코드가 복잡해지면서 예기치 못한 오류가 발생할 수 있음

- 가급적 사용하지 않는 것을 권장하며, 함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값을 사용 하는 것을 추천



### 함수 응용

#### 내장 함수

- 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음

#### map

- map(function, iterable)

- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)을 적용하고 그 결과를 map object로 반환

#### map 활용 사례

- 알고리즘 문제 풀이시 input 값들을 숫자로 바로 활용하고 싶을 때

#### filter

- filter(function, iterable)

- 순회 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환

#### zip

- zip(\*iterables)

- 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

#### lambda 함수

- 람다함수     lambda [parameter] : 표현식
  
  - 표현식을 계산한 결과값을 반환하난 함수로, 이름이 없는 함수여서 익명함수라고도 불림

- 특징
  
  - return문을 가질 수 없음
  
  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음

- 장점
  
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  
  - def를 사용할 수 없는 곳에서도 사용가능 

#### 재귀 함수

- 자기 자신을 호출하는 함수

- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렵하도록 작성

#### 재귀 함수 주의사항

- 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨

- 파이썬에서는 최대 재귀 깊이가 1000번으로 이를 넘을 시 Recursion Error가 발생

#### 반복문과 재귀 함수 비교

- 재귀 호출은 변수 사용을 줄여줄 수 있음

- 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림



### 모듈

#### 개요

- 모듈과 패키지

- 파이썬 표준 라이브러리

- 가상 환경

- 유용한 패키지와 모듈

- 사용자 모듈과 패키지

#### 모듈과 패키지

- 자주 기능들을 하나의 파일로 : 모듈(module)

- 다양한 파일을 하나의 폴더로 : 패키지(package)

- 다양한 패키지를 하나의 묶음으로 : 라이브러리(library)

- 이것을 관리하는 관리자 : pip

- 패키지의 활용 공간 : 가상환경

#### 모듈과 패키지

- 모듈 : 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 거

- 패키지 : 특정 기능과 관련 여러 모듈의 집합, 패키지 안에는 또 다른 서브 패키지를 포함

#### 모듈과 패키지 불러오기

```python
import module
from module import var, fucion, Class
from module import *

from pachage import module
from package.module import var, fuction, Class
```

#### 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장 함수
  
  - https://docs.python.org/ko/3/library/index.html

#### 파이썬 패키지 관리자(pip)

- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

#### 파이썬 패키지 관리자 명령어

- 패키지 설치
  
  - 최신 버전 / 특정 버전(==) / 최소 버전(>=)을 몇시하여 설치가능
  
  ```git
  $pip install SomePackage
  ```

- 패키지 삭제
  
  - pip는 패키지 업그레이드를 하는 경우 과거 버전을 자동을 지워줌
  
  ```git
  $pip uninstall SomePackage
  ```

- 패키지 목록 및 특정 패키지 정보
  
  ```git
  $pip list    # 패키지 목록
  $pip show SomePackage    # 특정 패키지 정보
  ```

- 패키지 관리하기 (나중에 실습하면서 익히기)
  
  ```git
  $ pip freeze > requirements.txt
  $ pip install -r requirements.txt
  ```

- 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함



### 사용자 모듈과 패키지

#### 패키지

- 모든 폴더에는 \_\_init\_\_.py를 만들어 패키지로 인식
  
  Python 3.3부터는 파일이 없어도 되지만, 하위 버전 호환 및 프레임워크 등에서의 동작을 위해 파일을 생성하는 것을 권장

#### 패키지 만들기

- 폴더 구조 : check.py에서 calculator의 tools.py의 기능을 사용
  
  my_package/
  
     \_\_init\_\_.py
  
     check.py
  
     calculator/
  
          \_\_init\_\_.py
  
          tools.py

#### 모듈 만들기 - calculator

- tools.py에 add 함수와 minus 함수 작성

#### 모듈 활용하기 - check

- 모듈을 활용하기 위해서 import 문을 통해 가져옴
  
  ```python
  from calculator import tools
  ```

#### 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우

- 복수의 프로젝트의 경우 버전이 상이 할 수 있는데 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리 할 수 있음

- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음

#### 가상환경 생성

- 가상환결을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨

```git
python -m venv < 폴더명 >  # venv virtual environment
```

#### 가상환경 활성화/비활성화

- windows 
  
  - 활성화 : <venv>\Scripts\activate.bat
  
  - 비활성화 : deactivate
