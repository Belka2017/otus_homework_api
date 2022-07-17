import pytest

from src.rectangle import Rectangle


class TestError(Exception):
   print('Тест пройден с ошибкой')


class TestRectangle:
    def test_calculate_area(self):
        rectangle = Rectangle(25, 30)
        rectangle_area = rectangle.area

        assert rectangle_area == 750, "Площадь прямоугольника рассчитана не верно"

    def test_calculate_area_float(self):
        rectangle = Rectangle(15.76, 56.89)
        rectangle_area = rectangle.area

        assert rectangle_area == 896.5864, "Площадь прямоугольника рассчитана не верно"

    def test_calculate_perimeter(self):
        rectangle = Rectangle(25, 30)
        rectangle_perimeter = rectangle.perimeter

        assert rectangle_perimeter == 110, "Периметр прямоугольника рассчитан не верно"

    def test_calculate_perimeter_float(self):
        rectangle = Rectangle(15.76, 56.89)
        rectangle_perimeter = rectangle.perimeter

        assert rectangle_perimeter == 145.3, "Периметр прямоугольника рассчитан не верно"

    @pytest.mark.parametrize('a, b', [
        (0, 5),
        (7, 0),
    ],
        ids=['a=0', 'b=0']
    )
    def test_side_is_zero(self, a, b):
        try:
            Rectangle(a, b)
        except ValueError:
            print("Прямоугольник не существует")
        else:
            raise TestError('Не отработало исключение, что сторона прямоугольника не может быть = 0')

    @pytest.mark.parametrize('a, b', [
        (-3, 5),
        (7, -4),
    ],
                             ids=['negative val a', 'negative val b']
                             )
    def test_side_is_negative_val(self, a, b):
        try:
            Rectangle(a, b)
        except ValueError:
            print("Прямоугольник не существует")
        else:
            raise TestError('Не отработало исключение, что сторона прямоугольника должна быть больше 0')

    @pytest.mark.parametrize('a, b', [
        ('pal', 5),
        (7, 'os'),
    ],
                             ids=['unavailable val a', 'unavailable val b']
                             )
    def test_side_is_str(self, a, b):
        try:
            Rectangle(a, b)
        except TypeError:
            print("Прямоугольник не существует")
        else:
            raise TestError('Не отработало исключение, что сторона задается целым или вещественным числом')

    @pytest.mark.parametrize('a, b', [
        (23, 23),
        (5.6, 5.6),
    ],
                             ids=['a=b int', 'a = b float']
                             )
    def test_is_not_rectangle(self, a, b):
        try:
            Rectangle(a, b)
        except ValueError:
            print("Эта фигура - квадрат")
        else:
            raise TestError('Не отработало исключение, проверяющее что фигура является квадратом')
