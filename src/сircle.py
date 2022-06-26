from math import pi

from src.figure import Figure


class Circle(Figure):
    def __init__(self, r, name='Circle'):
        self.verification_side(r)

        self.r = r
        self.name = name
        self._area = 0

    @classmethod
    def verification_side(cls, r):
        if r <= 0:
            raise ValueError("Радиус окружности не может быть меньше или равен 0")
        if type(r) != int and type(r) != float:
            raise TypeError("Значение разиуса окружности - целое или вещественное число")

    @property
    def area(self):
        self._area = pi * (self.r ** 2)
        return self._area

    @property
    def perimeter(self):
        return 2 * pi * self.r
    