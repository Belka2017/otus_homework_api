import pytest

from src.triangle import Triangle


class TestError(Exception):
   print('Тест пройден с ошибкой')


class TestTriangle:
    def test_calculate_area(self):
        triangle = Triangle(4, 5, 5)
        triangle_area = triangle.area

        assert triangle_area == 9.16515138991168, "Площадь теугольника рассчитана не верно"

    def test_calculate_area_float(self):
        triangle = Triangle(9.3, 9.4, 15.76)
        triangle_area = triangle.area

        assert triangle_area == 39.65690169932594, "Площадь теугольника рассчитана не верно"

    def test_calculate_perimeter(self):
        triangle = Triangle(14, 15, 13)
        triangle_perimeter = triangle.perimeter

        assert triangle_perimeter == 42, "Периметр треугольника рассчитан не верно"

    def test_calculate_perimeter_float(self):
        triangle = Triangle(14.345, 15.45654, 13.456)
        triangle_perimeter = triangle.perimeter

        assert triangle_perimeter == 43.257540000000006, "Периметр треугольника рассчитан не верно"

    @pytest.mark.parametrize('a, b, c', [
        (10, 3, 5),
        (7, 18, 10),
        (6, 7, 35),
    ],
        ids=['a>b+c', 'b>a+c', 'c>a+b']
    )
    def test_does_not_exist(self, a, b, c):
        try:
            Triangle(a, b, c)
        except ValueError:
            print("Треугольник не существует")
        else:
            raise TestError('Не отработало исключение, что сумма 2ух сторон должна быть больше 3ей')

    @pytest.mark.parametrize('a, b, c', [
        (0, 5, 5),
        (7, 0, 10),
        (6, 7, 0),
    ],
        ids=['a=0', 'b=0', 'c=0']
    )
    def test_side_is_zero(self, a, b, c):
        try:
            Triangle(a, b, c)
        except ValueError:
            print("Треугольник не существует")
        else:
            raise TestError('Не отработало исключение, что все стороны треугольника должны != 0')

    @pytest.mark.parametrize('a, b, c', [
        (-3, 5, 5),
        (7, -4, 10),
        (6, 7, -5),
    ],
                             ids=['negative val a', 'negative val b', 'negative val c']
                             )
    def test_side_is_negative_val(self, a, b, c):
        try:
            Triangle(a, b, c)
        except ValueError:
            print("Треугольник не существует")
        else:
            raise TestError('Не отработало исключение, что все стороны треугольника должны быть положительным')

    @pytest.mark.parametrize('a, b, c', [
        ('pal', 5, 5),
        (7, 'os', 10),
        (6, 7, '!@#$'),
    ],
                             ids=['unavailable val a', 'unavailable val b', 'unavailable val c']
                             )
    def test_side_is_str(self, a, b, c):
        try:
            Triangle(a, b, c)
        except TypeError:
            print("Треугольник не существует")
        else:
            raise TestError('Не отработало исключение, что сторона задается целым или вещественным числом')
