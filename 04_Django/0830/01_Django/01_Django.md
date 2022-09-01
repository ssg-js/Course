# 01 Django

## Framework

- 누군가 만들어 놓은 코드를 재사용 하는 것은 이미 익숙한 개발 문화

- 그렇다면 '웹 서비스'도 누군가 개발해 놓은 코드를 재사용하면 된다.

- **서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것** 

- 생산성과 품질을 높임

- Laravel, Django, Flask, Spring Boot 등

## Django를 배워야하는 이유

- Python으로 작성된 프레임워크

## WWW (World Wide Web)

- **전 세계에 퍼져 있는 거미줄 같은 연결망**

## 클라이언트-서버 구조

- 대부분의 웹 서비스는 클라이언트-서버 구조를 기반으로 동작

- 클라이언트 : 서비스를 요청하는 주체

- 서버 : 요청에 대해 서비스를 응답하는 주체

## 웹 페이지란?

- 정적 웹 페이지
  
  - 모든 사용자에게 동일한 모습으로 전달되는 것

- 동적 웹 페이지
  
  - 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
  
  - 웹 페이지의 내용을 바꿔주는 주체 == **서버**

## Design Pattern 이란?

- 자주 사용되는 구조가 있다는 것을 알게 되었고 이를 일반화해서 하나의 공법으로 만들어 둔 것

- 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙, 커뮤니케이션의 효율성을 높이는 기법

## Django에서의 디자인 패턴

- MTV 패턴 : MVC 디자인 패턴을 기반으로 조금 변형된 패턴이다.

- MVC 소프트웨터 디자인 패턴
  
  - Model : **데이터**와 관련된 로직을 관리
  
  - View : 레이아웃과 **화면**을 처리
  
  - Controller : 명령을 model과 view 부분으로 연결
  
  | MVC         | MTV      |
  | ----------- | -------- |
  | Model       | Model    |
  | View        | Template |
  | Controlloer | View     |

## Django Quick start

- vs code
  
  - 가상환경 만들기 : python -m venv venv
  
  - 가상환경 활성화 : source venv/Scripts/activate
  
  - 가상환경 비활성화 : deactivate
  
  - django 설치하기 : pip install django==3.2.13
    -> LTS(Long Term Support) : 장기 지원 버전
  
  - 가상환경 패키지 목록 조회 : pip list
  
  - requirements.txt 생성 : pip freeze > requirements.txt
  
  - requirements.txt 목록 설치 : pip install -r requirements.txt
    -> 용량이 크고 파일이 많은 venv 폴더를 git으로 올리지 않고 requirements 파일로 명시
  
  - django project 생성 : django-admin startproject firstpjt .
    -> . 을 넣어줘야 현재 폴더에 바로 만듬 안적으면 중첩으로 만들어짐
  
  - django 서버 실행 : python manage.py runserver
  
  - django 애플리케이션 생성 : python manage.py startapp articles
    -> 애플리케이션 생성시 영어 복수형으로 하는 것이 관례
  
  - INSTALLED_APPS에 앱을 등록(프로젝트 settings.py)
    -> 사용자 앱은 제일 위에 추가하는 걸 권장(앱 실행이 오류 방지)
    -> **반드시 생성 후 등록!!!!** 
  
  - /, , : 트레일링 슬래쉬, 콤마(확장성)
  
  - url.py에 path 등록
  
  - views.py에 함수 생성
  
  - templates 생성(vs code에서 materital Icon Them 설치)

## Django Template

- 데이터 표현을 제어하는 도구이자 표현에 관련되 로직

- Django Template Language (DTL)
  
  - 조건, 반복, 변수 치환, 필터 등의 기능을 제공

- Variable

- Filters

- Tags

- Comments

## Template inheritance

- 코드의 재사용성에 초점을 맞춤

- extends, block

- {% extends '' %}
  
  - 반드시 템플릿 최상단에 작성 되어야 함 (즉, 2개 이상 사용할 수 없음)

- {% block content %}{% endblock content %}
  
  - 하위 템플릭에서 재지정할 수 있는 블록을 정의

## form data로 데이터 주고받기

- \<form\>
  
  - 데이터가 전송되는 방법을 정의

- form's attributes
  
  - action : 어디에 전송? -> url
  
  - method : 어떻게 전송? -> 
    
    - get : 조회
    
    - post : 생성

## Django URLs

- 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작함

## Trailing Slashes

- URL 끝에 /가 없다면 자동으로 붙여주는 것이 기본 설정

- 모든 프레임워크가 그렇진 않음

## Variable routing



## Naming URL patterns



## 마무리

- "표현과 로직(View)을 분리"
  
  - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐

- "중복을 배제"
  
  - 
