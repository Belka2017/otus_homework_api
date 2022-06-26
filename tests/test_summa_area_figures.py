from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.сircle import Circle


class TestSummaAreaFigures:
    def test_sum_rectangle_and_square(self):
        rect = Rectangle(10, 20)
        sq = Square(30)
        area_rect = rect.area
        sq_area = sq.area
        exp_sum = area_rect + sq_area
        assert rect.add_area(sq) == exp_sum
        assert sq.add_area(rect) == exp_sum

    def test_sum_rectangle_and_triangle(self):
        rect = Rectangle(10, 20)
        tr = Triangle(10, 18, 17)
        area_rect = rect.area
        tr_area = tr.area
        exp_sum = area_rect + tr_area
        assert rect.add_area(tr) == exp_sum
        assert tr.add_area(rect) == exp_sum

    def test_sum_rectangle_and_circle(self):
        rect = Rectangle(10, 20)
        cr = Circle(17)
        area_rect = rect.area
        cr_area = cr.area
        exp_sum = area_rect + cr_area
        assert rect.add_area(cr) == exp_sum
        assert cr.add_area(rect) == exp_sum

    def test_sum_square_and_triangle(self):
        sq = Square(10)
        tr = Triangle(13, 15, 16)
        sq_area_ = sq.area
        tr_area = tr.area
        exp_sum = sq_area_ + tr_area
        assert sq.add_area(tr) == exp_sum
        assert tr.add_area(sq) == exp_sum

    def test_sum_square_and_circle(self):
        sq = Square(10)
        cr = Circle(16)
        sq_area = sq.area
        cr_area = cr.area
        exp_sum = sq_area + cr_area
        assert sq.add_area(cr) == exp_sum
        assert cr.add_area(sq) == exp_sum

    def test_triangle_and_circle(self):
        tr = Triangle(10, 13, 15)
        cr = Circle(16)
        tr_area = tr.area
        cr_area = cr.area
        exp_sum = tr_area + cr_area
        assert tr.add_area(cr) == exp_sum
        assert cr.add_area(tr) == exp_sum

    def test_figure_doesnt_exist(self):
        tr = Triangle(10, 13, 15)
        kr = tr.perimeter
        try:
            tr.add_area(kr)
        except ValueError:
            print("Переданная фигура не является геометрической или не была определена")

    def test_without_area(self):
        tr = Triangle(10, 13, 15)
        tr_area = tr.area
        sq = Square(10)

        assert tr.add_area(sq) == tr_area

    def test_without_area_2(self):
        tr = Triangle(10, 13, 15)
        sq = Square(10)

        assert tr.add_area(sq) == 0
