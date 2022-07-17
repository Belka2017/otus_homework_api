from src.figure import Figure


class Square(Figure):
    def __init__(self, a, name='Square'):
        self.verification_side(a)

        self.a = a
        self.name = name
        self._area = 0

    @classmethod
    def verification_side(cls, a):
        if a <= 0:
            raise ValueError("Сторона квадрата не может быть меньше или равна 0")
        if type(a) != int and type(a) != float:
            raise TypeError("Значение длины стороны квадрата - целое или вещественное число")

    @property
    def area(self):
        self._area = self.a ** 2
        return self._area

    @property
    def perimeter(self):
        return 4 * self.a
