# 02_Web

## Web이란

- 웹 사이타른 브라우저를 통해서 접속하는 웹 페이지(문서)들의 모음

## 웹 사이트 구성 요소

- HTML -> 구조

- CSS -> 표현

- Javascipt -> 동작

[설명](https://html-css-js.com/)

## 웹 사이트와 브라우저

- 웹 사이트는 브라우저를 통해 동작함

- 브라우저마다 동작이 약간씩 달라서 문제가 생김(파편화)

- 해결책으로 웹표준이 등장(USB 같이)

- .hwp .doc 같은 경우 MSword에서 깨지는 경우가 생김

## 웹 표준

- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)
- W3C

## HTML

- Hyper Text Martup Language(팀 버너스리)
- 저장과 처리가 없기 때문에 프로그래밍 언어가 아님!
- 요소 + 속성

## Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

- HTML, Markdown

## HTML 기본구조

- html : 문서의 최상위(root) 요소

- head : 문서 메타데이터 요소

- body : 본 문서 내용

### head 예시 : Open Graph Protocol

- 메타 데이터를 표현하는 새로운 규약

- 썸네일, 제목 등을 정의

## 요소(element)

- 시작 태그와 종료 태그 그리고 그 사이에 위치한 내용을 구성

- 닫는 태그가 없는 태그도 존재

- 중첩이 될 수 있음

## 속성(attribute)

- 태그의 디테일한 정보를 제공하기 위해 제공

## DOM(Document Object Model) 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조

## 인라인 / 블록 요소

- 인라인 요소는 글자처럼 취급(자기가 있는 공간만 취급)

- 블록요소는 한줄을 모두 사용

## 시맨틱 태그

- header, section, footer 등으로 역할 및 의미적 가치를 가지는 태그

## form

- 정보(데이터)를 서버에 제출하기 위해 사용하는 태그

## CSS

- Cascading Style Sheets (Cascading : 위에서 아래로 흐른다)

- 스타일을 지정하기 위한 언어

- 선택하고, 스타일을 지정

- 선택자, 결합자, display, position

- 예시 - h1 = 선택자, color: blue; = 선언, font-size = 속성, 15px = 값
  
  - ```html
    h1 {
        color: blue;
        font-size: 15px;
    }
    ```

## CSS 정의 방법

- 인라인(inline)

- 내부 참조(embedding) - head 에서 <style>

- 외부 참조(link file) - 분리된 CSS 파일 -> 가장 많이 쓰는 방식 
  
  - link:css 로 필요한 형식을 바로 불러올 수 있음

## 선택자

- 기본 선택자
  
  - 전체 선택자(\*), 요소 선택자(h1, h2,...)
  
  - 클래스 선택자(.{클래스}, **여러개** ), 아이디 선택자(#{아이디}, **한개만** 쓰기로 약속), 속성 선택자

## 결합자

- 자손 결합자(공백)
  
  - selectorA 하위의 모든 selectorB 요소

- 자식 결합자(>)
  
  - selectorA 바로 아래의 selectorB 요소

- 일반 형제 결합자(\~)
  
  - selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택

- 인접 형제 결합자(+)
  
  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

## Box model

- 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.(좌축 상단에 배치) -> **Normal Flow** 

- 하나의 박스는 네 부분(영역)으로 이루어짐
  
  - margin : 테두리 바깥의 외부 여백 배경색을 지정할 수 없다.
  
  - border : 테두리 영역
  
  - padding : 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용
  
  - content : 글이나 이미지 등 요소의 실제 내용

- div { display: block; } 으로 확인가능

# CSS Display

## CSS 원칙

- 모든 요소는 네모(박스모델)이고, 좌측상단에 배치.

- display에 따라 크기와 배치가 달라진다.

## 대표적으로 활용되는 display

- display: block
  
  - 줄 바꿈이 일어나는 요소
  
  - 화면 크기 전체의 가로폭을 차지한다
  
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음

- display: inline
  
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  
  - content 너비만큼 가로 폭을 차지한다.
  
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  
  - 상하 여백은 line-height로 지정한다.

- display: inline-block
  
  - 겉으로는 inline으로 존재하지만 내부적으로 block임
  
  - width, height 설정 가능

# CSS Position

- 문서 상에서 요소의 위치를 지정

- static : 모든 태그의 기본 값(기준 위치)
  
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

- 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능(position :)
  
  1) relative
  
  2) absolute
  
  3) fixed
  
  4) sticky

- relative : 상대 위치
  
  - static일때 공간은 남겨놓고 이동한다. 원래 공간은 차지하고 있지만 모습만 이동함
  
  - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음

- absolute : 절대 위치
  
  - 요소를 일반적인 문서 흐르메서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
  
  - **static이 아닌** 가장 가까이 있는 부모/조상 요소를 기준으로 이동( **없는 경우 브라우저 화면 기준으로 이동** )

- fixed : 고정 위치
  
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
  
  - 
