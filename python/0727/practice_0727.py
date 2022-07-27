# online_practice
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, type):
        self.name = name
        self.type = type
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def dead(self):
        Doggy.num_of_dogs -= 1

    def bark(self):
        return "멍"

    @classmethod
    def get_status(cls):
        return f"새로 태어난 개의 숫자 : {Doggy.birth_of_dogs}"
        return f"현재 있는 개의 숫자 : {Doggy.num_of_dogs}"


# homework
a = True
print(type(a))


# workshop
# 1
from faker import Faker  # 1 _faker 패키지에서 Faker 모듈을 사용_을 하기 위한 코드이다.

fake = Faker()  # 2 Faker는 _클래스_, fake는 _객체_이다.
fake.name()  # 3 name()은 fake의 _메서드_이다.

# 3


# 4
fake1 = Faker('ko_KR')
Faker.seed(87654321)

print(fake1.name())  # 1

fake2 = Faker('ko_KR')
print(fake2.name())  # 2

# 4-2
fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name())  # 1

fake2 = Faker('ko_KR')
print(fake2.name())  # 2
