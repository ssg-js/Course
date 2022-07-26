import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea):
    for i in range(3):
        sea[index - 1 + i] = 1


# 한 번의 공격을 피할 수 있는 함수
player_avoid = True  # avoid 사용 가능 상태, False면 한번 써서 못쓰는 상태
computer_avoid = True


def avoid(attack, sea):
    if sea[attack - 1] == 0:  # 왼쪽에 맞았을 경우
        sea[attack] = 0  # 오른쪽으로 이동
        try:
            for i in range(3):
                sea[attack + 1 + i] = 1
        except:
            return True  # 이동이 불가능하면 패배
    elif sea[attack + 1] == 0:  # 오른쪽에 맞았을 경우
        sea[attack] = 0  # 왼쪽으로 이동
        try:
            for i in range(3):
                sea[attack - 1 - i] = 1
        except:
            return True  # 이동이 불가능하면 패배
    elif sea[attack + 1] * sea[attack - 1]:  # 가운데에 공격받은 경우 패배
        return True
    return False  # 한번 피함


player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

round = 1  # 게임 라운드

# 1. 게임 준비
while True:
    # 1-1) 플레이어의 배 시작 위치 고르기
    player_index = int(input('배를 위치시킬 시작점을 고르세요.: ')) - 1

    # 1-2) 범위를 벗어난 시작점을 고른 경우
    if (player_index < 1) or (player_index > 13):
        print('-----해당 위치에는 배를 둘 수 없습니다.-----')
    else:
        break


# 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.
computer_index = random.randrange(1, 13)

# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기
set_ship(player_index, player_sea)
set_ship(computer_index, computer_sea)

# 2. 라운드 진행
while True:
    # 2-1) 플레이어 공격
    print('-' * 30)
    print('< Information Board >')
    print('플레이어의 해역: ', player_sea)
    print('플레이어의 공격 기록: ', player_attacked)

    # 2-2) 플레이어의 공격 위치 선택
    while True:
        player_attack_index = int(input('공격할 위치를 선택하세요. : ')) - 1

        if (player_attack_index < 1) or (player_attack_index > 13):
            print('해역의 범위에서 벗어난 위치를 선택하셨습니다. 다시 선택해 주세요.')
        elif player_attacked[player_attack_index] == True:
            print('이미 공격한 위치를 선택하셨습니다. 다시 선택해 주세요')
        else:
            break

    print(f'<{round}라운드 결과!>')
    # 2-3) 플레이어의 공격이 성공한 경우
    if computer_sea[player_attack_index] == 1:
        if computer_avoid:  # True 였다가 avoid 한번하거나 실패하면 False
            computer_avoid = avoid(player_attack_index, computer_sea)
        else:
            print('컴퓨터의 해역 : ', computer_sea)
            print(
                f'플레이어는 컴퓨터의 해역 {player_attack_index + 1}번째 칸을 공격하였고, 컴퓨터의 배는 피격되었습니다.'
            )
            print(f'게임이 종료되었습니다! {round}라운드 만에 플레이어의 승리입니다!')
            break
    # 2-4) 플레이어의 공격이 실패한 경우
    else:
        player_attacked[player_attack_index] = True

    # 2-5) 컴퓨터의 공격 위치 지정
    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트
    # 컴퓨터가 공격하지 않는 위치의 인덱스를 가져옴
    computer_not_attacked = [
        i for i in range(len(computer_attacked)) if (computer_attacked[i] == False)
    ]
    computer_attack_index = computer_not_attacked[
        random.randrange(len(computer_not_attacked))
    ]
    # 2-6) 컴퓨터의 공격이 성공한 경우
    if player_sea[computer_attack_index] == 1:
        if player_avoid:  # True 였다가 avoid 한번하거나 실패하면 False
            player_avoid = avoid(computer_attack_index, player_sea)
        else:
            print(
                f'플레이어는 컴퓨터의 해역 {computer_attack_index + 1}번째 칸을 공격하였으나, 공격에 실패하였습니다!'
            )
            print(
                f'컴퓨터는 플레이어의 해역 {computer_attack_index + 1}번째 칸을 공격하였고, 플레이어의 배는 피격되었습니다.'
            )
            print(f'게임이 종료되었습니다! {round}라운드 만에 컴퓨터의 승리입니다!')
            break
    # 2-7) 컴퓨터의 공격이 실패한 경우
    else:
        print(f'플레이어는 컴퓨터의 해역 {player_attack_index + 1}번째 칸을 공격하였으나, 공격에 실패하였습니다!')
        print(f'컴퓨터는 플레이어의 해역 {computer_attack_index + 1}번째 칸을 공격하였으나, 공격에 실패하였습니다!')
        computer_attacked[computer_attack_index] = True

    round += 1
