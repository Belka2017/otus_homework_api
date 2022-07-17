from src.square import Square


class TestError(Exception):
   print('Тест пройден с ошибкой')


class TestSquare:
    def test_calculate_area(self):
        square = Square(40)
        square_area = square.area

        assert square_area == 1600, "Площадь квадрата рассчитана не верно"

    def test_calculate_area_float(self):
        square = Square(45.9876)
        square_area = square.area

        assert square_area == 2114.85935376, "Площадь квадрата рассчитана не верно"

    def test_calculate_perimeter(self):
        square = Square(50)
        square_perimeter = square.perimeter

        assert square_perimeter == 200, "Периметр квадрата рассчитан не верно"

    def test_calculate_perimeter_float(self):
        square = Square(50.786)
        square_perimeter = square.perimeter

        assert square_perimeter == 203.144, "Периметр квадрата рассчитан не верно"

    def test_side_is_zero(self):
        try:
            Square(0)
        except ValueError:
            print("Квадрата не существует")
        else:
            raise TestError('Не отработало исключение, что сторона квадрата не может быть = 0')

    def test_side_is_negative_val(self):
        try:
            Square(-78)
        except ValueError:
            print("Квадрата не существует")
        else:
            raise TestError('Не отработало исключение, что сторона квадрата должна быть больше 0')

    def test_side_is_str(self):
        try:
            Square('fyhbvh')
        except TypeError:
            print("Квадрата не существует")
        else:
            raise TestError('Не отработало исключение, что сторона задается целым или вещественным числом')
