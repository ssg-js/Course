# Web 04. Grid System & Responsive Web

## 1. CSS flex-direciton

flex-direction

(a) row : main axis 를 가로로 왼쪽 위쪽부터 쌓이도록 설정

(b) column : main axis 를 세로로 왼쪽 위쪽부터 쌓이도록 설정

(c) row-reverse : main axis 를 가로로 오른쪽 위쪽부터 쌓이도록 설정

(d) column-reverse : main axis 를 세로로 왼쪽 아래쪽부터 쌓이도록 설정

## 2. Bootstrap flex-direction

flex-direction: row  -> flex-row

flex-direction: column -> flex-column

flex-direction: row-reverse -> flex-row-reverse

flex-direction: column-reverse -> flex-column-reverse

## 3. align-items

stretch : 플렉스 요소의 높이가 플렉스 컨테이너의 높이와 같게 변경된 뒤 연이어 배치됩니다.

center : 플렉스 요소는 플렉스 컨테이너의 가운데에 배치됩니다.

flex-start : 플렉스 요소는 플렉스 컨테이너의 위쪽에 배치됩니다.

flex-end : 플렉스 요소는 플렉스 컨테이너의 가운데에 배치됩니다.

baseline : 플렉스 요소는 플렉스 컨데이너의 기준선에 배치됩니다. 

## 4. flex-flow

flex-flow는 (1) flex-direction, flex-wrap 두 속성의 축약형이다.

## 5. Bootstrap Grid System

```html
<div class="(a)">
  <div class="(b)">
    <div class="col-(c)-(d)"></div>
  </div>
</div>
```

(a) container

(b) row

## 6. Breakpoint prefix

1\) 

| (c) | 의미                            | Container (max-width) |
| --- | ----------------------------- | --------------------- |
|     | (default) Extra small(<576px) | None (auto)           |
| sm  | Small(>=576px)                | 540px                 |
| md  | Medium(>=768px)               | 720px                 |
| lg  | Large(>=992px)                | 960px                 |
| xl  | Extra large(>=1200px)         | 1140px                |
| xxl | Extra extra large(>=1400px)   | 1320px                |

2\) (d) 에는 숫자가 들어갑니다. 가로전체 비율은 12이고 숫자에 맞는 비율로 정합니다. (b)의 breakpoint 조건에 맞으면 (d)의 숫자대로 너비비율이 정해집니다.
