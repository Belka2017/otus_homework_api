from src.сircle import Circle


class TestError(Exception):
   print('Тест пройден с ошибкой')


class TestCircle:
    def test_calculate_area(self):
        circle = Circle(120)
        circle_area = circle.area

        assert circle_area == 45238.93421169302, "Площадь круга рассчитана не верно"

    def test_calculate_area_float(self):
        circle = Circle(45.9876)
        circle_area = circle.area

        assert circle_area == 6644.0266091480735, "Площадь круга рассчитана не верно"

    def test_calculate_perimeter(self):
        circle = Circle(50)
        circle_perimeter = circle.perimeter

        assert circle_perimeter == 314.1592653589793, "Периметр круга рассчитан не верно"

    def test_calculate_perimeter_float(self):
        circle = Circle(50.786)
        circle_perimeter = circle.perimeter

        assert circle_perimeter == 319.09784901042246, "Периметр круга рассчитан не верно"

    def test_side_is_zero(self):
        try:
            Circle(0)
        except ValueError:
            print("Круга не существует")
        else:
            raise TestError('Не отработало исключение, что радиус круга не может быть = 0')

    def test_side_is_negative_val(self):
        try:
            Circle(-78)
        except ValueError:
            print("Круга не существует")
        else:
            raise TestError('Не отработало исключение, что радиус круга должен быть больше 0')

    def test_side_is_str(self):
        try:
            Circle('fyhbvh')
        except TypeError:
            print("Круга не существует")
        else:
            raise TestError('Не отработало исключение, что радиус круга задается целым или вещественным числом')
