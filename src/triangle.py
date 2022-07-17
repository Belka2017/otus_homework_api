from math import sqrt

from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c, name='Triangle'):
        self.verification_side(a, b, c)

        self.a = a
        self.b = b
        self.c = c
        self.name = name
        self._area = 0

    @classmethod
    def verification_side(cls, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Сторона треугольника не может быть меньше или равна 0")
        if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float) or \
                (type(c) != int and type(c) != float):
            raise TypeError("Значение длины стороны треугольника - целое или вещественное число")
        if a + b < c:
            raise ValueError("Треугольника не существует, так как сумма 2ух сторон меньше третьей")
        if a + c < b:
            raise ValueError("Треугольника не существует, так как сумма 2ух сторон меньше третьей")
        if b + c < a:
            raise ValueError("Треугольника не существует, так как сумма 2ух сторон меньше третьей")

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter / 2
        self._area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return self._area
