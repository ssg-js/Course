def solution(places):
    answer = []
    
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]


    for place in places:
        result = 1
        for i in range(5):
            print()
            for j in range(5):
                # 응시자 주위에 테이블만 지나서 맨해튼 거리 2 안에 사람이 있는지 확인
                if place[i][j] == 'P':
                    temp = 0
                    ni = i
                    nj = j
                    while result and temp < 2:
                        # 상하좌우로 이동
                        d = 0
                        while result and d < 4:
                            ni += di[d]
                            nj += dj[d]
                            # 한 번 이동하고 원래 있던 p로 가면 안되므로
                            if ni != i or nj != j:
                                if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'O':
                                    break  # 테이블이면 이동한 위치 유지
                                elif 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                                    result = 0  # 한번 거리두기를 어기면 모든 반복문 나감
                                    break
                            ni -= di[d]
                            nj -= dj[d]
                            d += 1
                        temp += 1
                if result == 0:
                    break
            if result == 0:
                break
        answer.append(result)
    return answer
