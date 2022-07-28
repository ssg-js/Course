# Python 08. 객체 지향 프로그래밍

## 1. 도형 만들기

```python
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

```
