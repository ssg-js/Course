# Web

## CSS layout

- css 원칙 : Inline Direction, Block Direction -> 좌측상단부터 쌓임(Normal Flow)

- 모든요소는 네모(박스모델)이고

- 어떤 요소를 감싸는 형태의 배치는????
  혹은 좌/우칙에 배치는???

### Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 Wrapping 하도록 함

- 요소가 Normal flow를 벗어남

- none, left, right 속성있음

### z-index

### Flexible Box Layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

- internet explorer 는 쓰기 힘듬

- display : flex (아이템에 플렉스를 적용하는게 아님 부모요소에 적용해야함)

- main axis

- cross axis(main axis와 수직)

- inline-flex 도 있음

- flex-direction : row (or column)

### Flex 속성

- 배치 설정 : flex-direction, flex-wrap

- 공간 나누기 : justify-content(main axis), align-content(cross axis)

- 정렬 : align-items

### Flex 속성 : flex-direction

- 역방향의 경우 HTML태그 선언 순서와 시각적으로 다르니 유의(웹 접근성에 영향)

### Flex 속성 : flex-wrap

- 요소가 잘리거나 잘리지 않게 다 담기도록 함

### Flex 속성 : flex-flow

- flex-flow: row nowrap (이렇게 사용가능)

### Flex 속성 : justify-content

### Flex 속성 : align-content

### Flex-grow & order


