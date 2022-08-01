# 1
from sys import int_info


def count_vowels(word):
    count = 0
    for v in ['a', 'e', 'i', 'o', 'u']:
        count += word.count(v)
    return count


# 2

# 3 정사각형만 만들기
def only_square_area(widths, heights):
    square_value = []
    for width in widths:
        for height in heights:
            if height == width:  # 너비와 높이가 같을 때 넓이 값 저장
                square_value.append(width**2)
    return square_value


# workshop
# 1
def get_dict_avg(subject_scores):
    score_sum = 0
    for score in subject_scores.values():
        score_sum += score
    return score_sum / len(subject_scores)


# 2
def count_blood(bloods):
    type_count = {}  # 각 혈액형별 사람수를 저정하는 딕셔너리
    for blood in ['A', 'B', 'O', 'AB']:
        type_count[blood] = bloods.count(blood)
    return type_count


# online_practice
def leap_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return f'{year}는 윤년입니다.'
    else:
        return f'{year}는 윤년이 아닙니다.'
