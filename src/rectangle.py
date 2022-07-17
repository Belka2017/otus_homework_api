from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b, name='Rectangle'):
        self.verification_side(a, b)

        self.a = a
        self.b = b
        self.name = name
        self._area = 0

    @classmethod
    def verification_side(cls, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Сторона прямоугольника не может быть меньше или равна 0")
        if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
            raise TypeError("Значение длины стороны прямоугольника - целое или вещественное число")
        if a == b:
            raise ValueError("Фигура с заданными параметрами является квадратом")

    @property
    def area(self):
        self._area = self.a * self.b
        return self._area

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)
