import pytest

from creational.factory_method import ShapeCreator


class TestShapeFactory:
    def test_it_creates_circle(self):
        circle = ShapeCreator().shape_factory('circle', radius=3)

        assert circle.get_area() == 28.274
        assert circle.get_perimeter() == 18.85
        assert circle.get_type() == 'Circle'

    def test_it_creates_triangle(self):
        square = ShapeCreator().shape_factory('triangle', side1=4, side2=3, side3=2)

        assert square.get_area() == 2.905
        assert square.get_perimeter() == 9
        assert square.get_type() == 'Triangle'

    def test_it_creates_square(self):
        square = ShapeCreator().shape_factory('square', height=3)

        assert square.get_area() == 9
        assert square.get_perimeter() == 12
        assert square.get_type() == 'Square'

    def test_it_creates_rectangle(self):
        rectangle = ShapeCreator().shape_factory('rectangle', height=3, width=2)

        assert rectangle.get_area() == 6
        assert rectangle.get_perimeter() == 10
        assert rectangle.get_type() == 'Rectangle'

    def test_it_raises_excecption_if_invalid_shape_name(self):
        with pytest.raises(ValueError):
            ShapeCreator().shape_factory('invalid_shape_name', whatever=13)
