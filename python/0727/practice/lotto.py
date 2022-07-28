# 여기에 필요한 모듈을 추가합니다.
import random
import json


class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):

        for i in range(n):
            num = 0  # 번호 개수 세는 변수
            self.number_lines.append(random.sample(range(1, 46), 6))

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year, month, day = self.get_draw_date(draw_number)
        print('=' * 32)
        print(f'{"제 "+ str(draw_number) + "회 로또":^32}')
        print('=' * 32)
        print(f'추첨일 : {year}/{month}/{day} ')
        for i, numbers in enumerate(self.number_lines):
            alpha = chr(ord('A') + i)
            print(f'{alpha} : {numbers}')

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        main_numbers, bonus_number = self.get_lotto_numbers(draw_number)[0:2]
        print('=' * 32)
        print(f'{main_numbers} + {bonus_number}')
        print('=' * 32)
        for i, line in enumerate(self.number_lines):
            same_main_counts, is_bonus = self.get_same_info(
                main_numbers, bonus_number, line
            )[0:2]
            alpha = chr(ord('A') + i)
            ranking = self.get_ranking(same_main_counts, is_bonus)
            status = alpha + ' : ' + str(same_main_counts) + '개 '
            if bonus_number:
                status += '+ 보너스 일치 '
                if ranking == 1:
                    status += '(' + str(ranking) + '등 당첨!)'
                elif ranking == 2:
                    status += '(' + str(ranking) + '등 당첨!)'
                elif ranking == 3:
                    status += '(' + str(ranking) + '등 당첨!)'
                elif ranking == 4:
                    status += '(' + str(ranking) + '등 당첨!)'
                elif ranking == 5:
                    status += '(' + str(ranking) + '등 당첨!)'
                else:
                    status += '(낙첨)'
            else:
                status += '일치 '
                if ranking == 1:
                    status += '(' + str(ranking) + '등 당첨!)'
                elif ranking == 2:
                    status += '(' + str(ranking) + '등 당첨!)'
                elif ranking == 3:
                    status += '(' + str(ranking) + '등 당첨!)'
                elif ranking == 4:
                    status += '(' + str(ranking) + '등 당첨!)'
                elif ranking == 5:
                    status += '(' + str(ranking) + '등 당첨!)'
                else:
                    status += '(낙첨)'
            print(status)

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        info = open(f'data/lotto_{str(draw_number)}.json', encoding='utf-8')
        date = json.load(info)['drwNoDate']
        date = date.split('-')
        year, month, day = date[0:3]

        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        main_numbers = []
        info = open(f'data/lotto_{str(draw_number)}.json', encoding='utf-8')
        value = json.load(info)
        for k, v in value.items():
            if k.startswith('drwt'):
                main_numbers.append(v)
            else:
                if k.startswith('bnusNo'):
                    bonus_number = v
                else:
                    continue
        main_numbers.sort()

        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        is_bonus = False
        for line_number in line:
            for main_number in main_numbers:
                if line_number == main_number:
                    same_main_counts += 1
                else:
                    continue
            if line_number == bonus_number:
                is_bonus = True
            else:
                continue

        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        if same_main_counts == 6:
            ranking = 1
        elif (same_main_counts == 5) and is_bonus:
            ranking = 2
        elif same_main_counts == 5:
            ranking = 3
        elif same_main_counts == 4:
            ranking = 4
        elif same_main_counts == 3:
            ranking = 5
        else:
            ranking = -1
        return ranking
