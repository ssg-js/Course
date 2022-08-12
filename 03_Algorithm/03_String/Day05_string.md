# 문자열

## 문자의 표현

- 비트 컴퓨터의 아작 작은 단위(0, 1) -> 너무 작음

- 8bit -> 1byte 가 정보의 최소 단위가 됨(2의 8승)

- **아스키 코드** 는 8bit중 7bit를 써서 128문자를 표현

- 자국의 코드체계를 타국가가 가지고 있지 않으면 정보를 잘못 해석

- 그래서 국제 코드인 **유니코드** 가 나옴

- 유니코드는 **16진수** 이기 때문에 컴퓨터를 위한 **2진수** 변환이 필요함

- 그래서 **유니코드 인코딩(UTF: Uniconde Transformation Format)** 가 나옴
  
  - UTF-8 (in web) - 8bit에 넣는방법
    
    \- MIN : 8bit, MAX: 32bit(1 Byte * 4)
  
  - UTF-16 (in windows, java) 
    
    \- MIN : 16bit, MAX: 32bit(2 Byte * 2)
  
  - UTF-32 (in unix)
    
    \- MIN : 32bit, MAX: 32bit(4 Byte * 1)

## 문자열의 분류

- 문자열 : 컨테이너 > 시퀀스 > 불변형 > iterable

- 인덱싱, 슬라이싱 가능

## 문자열 뒤집기(Palindrome)

- 반복문 이용

- reverse 이용 : 문자열 -> 리스트 -> 거꾸로 -> 문자열

- slicing 이용 : string[::-1 ]

## 패턴 매칭

- 고지식한 패턴 검색 알고리즘

- 


