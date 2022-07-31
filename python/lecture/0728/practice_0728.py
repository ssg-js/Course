# course
from types import ClassMethodDescriptorType


class Person:
    counts = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call_name(self):
        return f'대전 2반 {self.name} 입니다!'

    @staticmethod
    def hello():
        return '안녕하세요!'


class Student(Person):
    @staticmethod
    def call_name(name):
        return f'대전 2반 {name} 입니다!'


person1 = Person("김성준", 25)
student1 = Student("박승재", 25)
print(student1.call_name("김진호"))


# hws
# 1
class Circle:
    pi = 3.14

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return Circle.pi * self.r * self.r

    def circumference(self):
        return 2 * Circle.pi * self.r

    def center(self):
        return (self.x, self.y)


circle = Circle(3, 2, 4)
print(circle.area())
print(circle.circumference())


# 2
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):
    def run(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')


dog = Dog('꼽이')
dog.run()  # 꼽이! 달린다!
dog.bark()  # 꼽이! 짖는다!
bird = Bird('구구')
bird.walk()  # 구구! 걷는다!
bird.eat()  # 구구! 먹는다!
bird.fly()  # 구구! 푸드덕!


# 3


# workshop
# 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)

    def get_perimeter(self):
        return (abs(self.p1.x - self.p2.x) * 2) + (abs(self.p1.y - self.p2.y) * 2)

    def is_square(self):
        if abs(self.p1.x - self.p2.x) == abs(self.p1.y - self.p2.y):  # 밑변과 높이가 같은 경우
            return True
        else:  # 다른 경우
            return False


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())


# online_practice
from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(self, name, birth):
        self.name = name
        self.birth = birth

    def check_age(self):
        year = datetime.now().year

        if self.age > 19 or self.birth < (year - 19):  # 현재년도(2022) - 19 = 2003
            return False
        else:  # 미성년자인 경우 True
            return True


js = Person('진성', 20)
js.details('진성', 2002)
print(js.check_age())

#
import random

frutes = ('사과', '귤', '포도', '배')
s = random.sample(frutes, 2)
print(s)  # ['배', '사과']

num = 4
status = str(num) + '개 있고 무러무라'
print(f'{status} 가 출력이될까')
