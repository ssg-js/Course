# SQLD

#### SQL 명령문 개괄

- From-where-groupby-having-select-orderby

- DML - select, insert, delete, update
  
  DDL - alter, create, modify, drop
  
  TCL - rollback, commit
  
  DCL - grant, revoke

#### select

- distinct (집약)
  
  - 중복된 값을 제거하고 집약
  
  - 예시)  DISTINCT depth,mgr -> (depth, mgr)에 대해 집약 == group by (depth,mgr)

- alias
  
  - AS 
    
    - select
      
      1) as 생략가능
      
      2) column명에 띄어쓰기 있는 경우, ex) "직원 번호"
    
    - from 
      
      1) as **사용불가!!!**

- concat 연산자 ( concat(().()) )
  
  - "+" : sql server
  
  - "=" : oracle
  
  - 인수가 반드시 **2개!**

#### 논리연산자

- 연산순위
  
  - not > and > or

- and
  
  - A and B

- or
  
  - A or B

- not
  
  - not A, B

#### SQL 연산자

- A **Between** B **and** C : B <= A <= C

- A **In** (1,2,3,) : A = 1 or A = 2 or A = 3

- **LIKE**
  
  - 와일드 카드
    
    - "\_" : 한 글자
    
    - "%" : 0개 이상의 글자
  
  - escape
    
    - ex) ename like 'A_A'
      
      LIKE escape 와일드카드(\_, %)를 문자로 취급!
      
      -> like 'A@\_A' ESCAPE '@' -> @는 아무문자나 가능!!

- Rownum(oracle)
  
  - where 조건절에서 Rownum = 1인 경우 포함
  
  - **select** empno, sal **from** emp **where** rownum <= 3 **order by** sal **desc**
    
    -> order by sal 이 가장 마지막
    
    -> 정렬 전에 rownum에 대해 먼저 실행 후 sal 순서로 정렬

- Top(sql server)
  
  - select top (n) <컬럼명> : 상위 n개

(19:13)
