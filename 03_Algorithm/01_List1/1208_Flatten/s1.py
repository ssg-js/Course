import sys

sys.stdin = open('input.txt')

# 버블 정렬을 변형해서 한 바퀴 돌아서 최댓값을 구하고 반대로 
# 한 바퀴 돌아서 최솟값을 구해서 덤프
for tc in range(1, 10):
    dump = int(input())
    yellow_boxes = list(map(int, input().split()))
    
    sub_box = 0

    # 주어진 덤프 수만큼 덤프
    for d in range(dump):
        for i in range(1, len(yellow_boxes)):
            # 최댓값이 리스트 제일 오른쪽으로
            if yellow_boxes[i-1] > yellow_boxes[i]:
                yellow_boxes[i-1], yellow_boxes[i] = yellow_boxes[i], yellow_boxes[i-1]
            # 최솟값이 리스트 제일 왼쪽으로
            if yellow_boxes[-i] < yellow_boxes[-i-1]:
                yellow_boxes[-i], yellow_boxes[-i-1] = yellow_boxes[-i-1], yellow_boxes[-i]
        # 최고점에서 최저점으로 옮기기
        yellow_boxes[-1] -= 1
        yellow_boxes[0] += 1

        # 한번 더
        for i in range(1, len(yellow_boxes)):
            # 최댓값이 리스트 제일 오른쪽으로
            if yellow_boxes[i-1] > yellow_boxes[i]:
                yellow_boxes[i-1], yellow_boxes[i] = yellow_boxes[i], yellow_boxes[i-1]
            # 최솟값이 리스트 제일 왼쪽으로
            if yellow_boxes[-i] < yellow_boxes[-i-1]:
                yellow_boxes[-i], yellow_boxes[-i-1] = yellow_boxes[-i-1], yellow_boxes[-i]

        # 최고점과 최저점 차이 구하기
        sub_box = yellow_boxes[-1] - yellow_boxes[0]

        if sub_box <= 1:
            break

    print(f'#{tc} {sub_box}')
