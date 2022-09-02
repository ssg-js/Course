# Queue

## 큐의 특성

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조 -> 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조

- 선입선출구조(FIFO)

## 큐의 선입선출 구조

- 머리(Front) : 저장된 원소 중 첫 번째 원소

- 꼬리(Rear) : 저장된 원소 중 마지막 원소

- enQueue : 삽입

- deQueue : 삭제

## 큐의 연산과정

1) 공백 큐 생성 : front = rear = -1

2) 원소 A 삽입 : front = -1, rear = 0

3) 원소 B 삽입 : front = -1, rear = 1

4) 원소반환/삭제 : front = 0, rear = 1

5) 원소 C 삽입 : front = 0, rear = 2

6) 원소반환/삭제 : front = 1, rear = 2

7) 원소반환/삭제 : front = rear = 2 -> front와 rear가 같으면 큐가 비어있는 상태
   
   

## 선형 큐

- 1차원 배열을 이용한 큐
  
  - 큐의 크기 == 배열의 크기

- 상태 표현
  
  - 초기 상태 : front = rear = -1
  
  - 공백 상태 : front == rear 
  
  - 포화 상태 : rear == n-1(n : 배열의 크기)

- 초기 공백 큐 생성
  
  - 크기 n인 1차원 배열 생성
  
  - front와 rear를 -1로 초기화

### 삽입

- rear += 1 후 rear 위치에 원소 추가

### 삭제

- front += 1 후 front 위치의 원소 삭제

### 검색 : Qpeek()

-  가장 앞에 있는 원소를 검색하여 반환하는 연산

- front + 1에 있는 원소를 반환

## 원형 큐

### 선형큐 이용시의 문제점

- 배열의 앞부분에 공간이 남아있음에도 불구하고 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨
  
  - 해결방법1
    
    매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동
  
  - 해결방법2
    
    1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형형태의 큐를 이룬다고 가정하고 사용

### front 변수

- 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

|     | 삽입 위치                   | 삭제 위치                     |
| --- | ----------------------- | ------------------------- |
| 선형큐 | rear = rear + 1         | front = front + 1         |
| 원형큐 | rear = (rear + 1) mod n | front = (front + 1) mod n |



## 우선순위 큐

- 우선순위를 가진 항목들을 저정하는 큐

- FIFO의 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.

- 적용 분야
  
  - 시뮬레이션 시스템
  
  - 네트워크 트래픽 제어
  
  - 운영체제의 테스크 스케줄링

### 구현

- 배열을 이용한 우선순위 큐

- 리스트를 이용한 우선순위 큐 (동적할당 linked list를 이용한 구현)

### 배열을 이용한 우선순위 큐

- 배열을 이용하여 자료 저장

- 가장 앞에 최고 우선순위의 원소가 위치하게 됨

- 문제점
  
  - 배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생 -> 이에 소요되는 시간이나 메모리 낭비가 큼
    
    

## 버퍼

- 데이터를 한 곳에서 다른 한 곳에서 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역

- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미

### 버퍼의 자료구조

- 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용된다.

- 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용된다.



## BFS(Breadth First Search)

- 너비 우선 탐색(bfs)

- 너비우선 탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
  
  