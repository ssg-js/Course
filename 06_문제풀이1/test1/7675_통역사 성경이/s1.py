import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    num = int(input())
    # 세 가지 구두점을 하나로 통일해서 나누기
    text = input().replace('?', '.').replace('!', '.')
    text = text.split('.')
    
    result = []
    for i in range(num):
        words = text[i].split()
        cnt = 0  # 이름의 개수 카운트
        # 한 문장의 단어를 검사
        for word in words:
            # 단어의 첫 알파벳이 대문자일때 나머지 소문자인지 검사
            if word[0].isupper():
                for c in word[1:]:
                    if c.isupper() or c.isdigit():
                        break
                else: # 첫 알파벳빼고 다 소문자일 경우
                    cnt += 1
        result.append(cnt)
    print(f'#{t}', *result)
    
