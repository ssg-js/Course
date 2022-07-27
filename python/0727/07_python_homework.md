# Python 07. 객체 지향 프로그래밍

## 1. Type Class

int, float, str, type, bool

## 2. Magic Mothod

\_\_inti\_\_ : 생성자, 해당 객체가 생성될 때 자동으로 호출됩니다.

\_\_del\_\_ : 소멸자, 객체가 소멸할 때 자동으로 호출됩니다.

\_\_str\_\_ : 해당 객체의 출력 형태를 지정, 프린트(print) 함수를 호출할 때 자동으로 호출됩니다.

\_\_repr\_\_ : 실제 값이 아닌 고유한 메모리 주소값을 반환합니다.

## 3. instance Method

.append() : 리스트에 원소를 추가합니다.

.pop() : default로 마지막 값을 반환하고 원래 리스트나 딕셔너리에서 없앱니다.

.count() : 문자열과 리스트에서 해당 값의 개수를 반환합니다.

## 4. 오류의 종류

ZeroDivisionError : 0으로 나눴을 때 오류

NameError : 변수 이름이 틀리거나 없는 변수르 사용할 때 오류

TypeError : 데이터 유형이 맞지 않을 경우의 오류

IndexError : 범위를 벗어난 인덱스 사용시 오류

KeyError : 딕셔너리 키가 없을 경우 오류

ModuleNotFoundError : import 되지 않은 모듈이나 잘못된 모듈을 사용했을시 오류

ImportError : import 시 설치되지 않거나 없는 모듈을 사용시 오류
