# Vue with DRF



## INDEX

- Vue with DRF

- CORS

- CRF Auth System

- DRF Auth with 



#### 개요

- server 와 client 의 통신



## Server & Client

#### Server

- 서버란? 
  
  - 클라이언트에게 <mark>**정보**</mark>와 <mark>**서비스**</mark>를 제공
  
  - 서비스 전체를 제공
  
  - 정보를 제공

- 서비스 전체를 제공 == Django Web Service
  
  - 모드 데이터가 포함됨 
  
  - 새로고침해야함

- 정보를 제공 == DRF API Service
  
  - Django를 통해 관리하는 정보만을 클라이언트에게 제공
  
  - DRF를 사용하여 JSON으로 변환

#### Client

- 클라이언트란?
  
  - <mark>**server가 제공하는 서비스에 적절한 요청**</mark>을 통해 <mark>**server로부터 반환 받은 응답을 사용자에게 표현**</mark>하는 기능을 가진 프로그램 혹은 시스템

- Server가 제공하는 서비스에 적절한 요청
  
  - Server가 정의한 방식대로 요청 인자를 넘겨 요청

- 잘못된 요청
  
  - 잘못된 filed명으로  요청을 보낼 경우 처리할 수 없음

#### 정리

- Server는 정보와 서비스를 제공
  
  - DB와 통신하며 데이터를 생성, 조회, 수정, 삭제를 담당
  
  - 요청을 보낸 Client에게 정상적인 요청이었다면 처리한 결과를 응답



- Client는 사용자의 정보 요청을 처리, server에게 응답 받은 정보를 표현
  
  - Server에게 정보(데이터)를 요청
  
  - 응답 받은 정보를 가공하여 화면에 표현

## CORS

#### what happened?

- 브라우저가 요청을 보내고 서버의 응답이 브라우저에 도착

- 보안상의 이유로 브라우저는 <mark>**동일 출처 정책(SOP)**</mark>에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한 함( 크롬이 막음 '엇 같은 vue가 아니네?' )

#### SOP (Same-Origin Policy)

- "동일 출처 정책"

- 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안 방식

- 공격받을 경로를 줄임

#### Origin - 출처

- <mark>**URL의 Protocol, Host, Port를 모두 포함**</mark>하여 **출처**라고 부름

- Same Origin 예시
  
  - 아래 세 영역이 일치하는 경우에만 동일 출처로 인정 
    
    ![](Vue%20with%20DRF_assets/2022-11-14-11-11-53-image.png)

#### CORS - 교차 출처 리소스 공유

- Cross-Origin Resources Sharing

- 추가 <mark>**HTTP Header**</mark>를 사용하여, 특정 출처에서 실행 중인 웹 어플리케이션이 <mark>**다른 출처의 자원에 접근할 수 있는 권한**</mark>을 부여하도록 브라우저에 알려주는 체제
  
  - 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 <mark>**서버에 지정**</mark>할 수 있는 방법

- 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행
  
  - 만약 다른 출처의 리소스를 가져오기 위해서는이를 제공하는 서비가 **브라우저에게** 다른 출처지만 접근해도 된다는 사실을 알려야 함
  
  - " 교차 출처 리소스 공유 정책 "

- Server에서 응답을 주더라도 브라우저에서 거절

- 그 출처에서 올바른 CORS header를 포함한 응답을 반환해함 함 (**서버**)

- https://developer.mozilla.org/ko/docs/Web/HTTP/CORS

#### How to set CORS

- HTTP Response Header 예시
  
  - <mark>**Access-Control-Allow-Origin**</mark>
    
    - 단일 출처를 지정하여 브라우저가 해당 출처가 리소스에 접근하도록 

#### django-cors-headers-library

[GitHub - adamchainz/django-cors-headers: Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS)](https://github.com/adamchainz/django-cors-headers)[GitHub - adamchainz/django-cors-headers: Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS)](https://github.com/adamchainz/django-cors-headers)

## Authentication & Authorization

#### Authentication - 인증, 입증

- 자신이라고 주장하는 사용자가 누구인지 확인

- 401 Unauthorized

#### Authorization - 권한 부여, 허가

- 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함
  
  - 사용자는 조직에 대한 엑세스 권한을 부여 받기 전에 먼저 자신의 ID가 진짜인지 먼저 확인해야 함

- 403 Forbidden
  
  - 401과 다른 점은 서버는 클라이언트가 누구인지 알고 있음

#### 인증 여부 확인 방법

- DRF 공식문서에서 제안하는 인증 절차 방법
  
  - https://www.django-rest-framework.org/api-guide/authentication/

- BasicAuthentication, SessionAuthentication 은 뭘까?

- settings.py에 작성하여야 할 설정
  
  - "기본적인 인증 절차를 어떠한 방식으로 둘 것이냐"를 설정하는 것

- 우리가 사용할 방법은 DRF가 기본으로 제공해주는 인증 방식 중 하나인 <mark>**TokenAuthentication**</mark>

- 모든 상황에 대한 인증 방식을 정의 하는 것이므로, 각 요청에 따라 인증 방식을 거치고자 한다면 다른 방식이 필요

- view 함수마다 다른 인증 방식을 설정하고 한다면 decorator 활용
  
  ![](Vue%20with%20DRF_assets/2022-11-14-15-09-44-image.png)

- [참고] permission_classes
  
  - 권한 관련 설정
  
  - 권한 역시 특정 view 함수마다 다른 접근 권한을 요구 할 수 있음

#### 다양한 인증 방식

- BasicAuthentication

- SessionAuthentication

- RemoteUserAuthenticaiton

- TokenAuthentication
  
  - 매우 간단한게 구현 할수 있음

- (중요) settings.py에서 DEFAULT_AUTHENTICATION_CLASSES를 정의 
  
  - TokenAuthentication 인증 방식을 사용할 것임을 명시

#### TokenAuthentication 사용 방법

- 생성한 Token을 각 User에게 발급

- User는 발급 받은 Token을 headers에 담아 요청과 함께 전송
  
  - 단 반드시 <mark>**Token**</mark> 문자열 함께 삽입

- 주의) Token 문자열과 발급받은 실제 token 사이를<mark>**' '(공백)**</mark>으로 구분
  
  ![](Vue%20with%20DRF_assets/2022-11-14-15-15-26-image.png)

## dj-rest-auth

- 회원가입, 인증(소설미디어 인증 포함), 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등을 위한 REST API and point 제공

- 주의) django-rest-auth는 더이상 업데이트 지원하지 않음

- https://github.com/iMerica/dj-rest-auth

- key : 833b13e91230933b4960d189d2c592147d3266f5

#### Permission setting

- DRF 공식문서 
