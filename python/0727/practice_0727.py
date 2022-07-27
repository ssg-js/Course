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
