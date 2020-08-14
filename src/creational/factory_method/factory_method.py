import abc
from math import pi, sqrt

from structural.decorator import round_decimals


class ShapeCreator:
    @staticmethod
    def shape_factory(name, **kwargs):
        """
        Factory method to create a shape given the name and the parameters needed for each shape
        :param name: Name of the shape
        :param kwargs: Parameter depending on the shape
        :return:
        """
        if name == 'circle':
            return Circle(**kwargs)
        elif name == 'triangle':
            return Triangle(**kwargs)
        elif name == 'square':
            return Square(**kwargs)
        elif name == 'rectangle':
            return Rectangle(**kwargs)
        else:
            raise ValueError('Invalid shape name')


class Shape(metaclass=abc.ABCMeta):
    """
    Abstract class with common methods for the shapes
    """
    @abc.abstractmethod
    def get_area(self):
        """
        Return the area of the shape
        :return: Area of the shape
        """
        pass

    @abc.abstractmethod
    def get_perimeter(self):
        """
        Return the perimeter of the shape
        :return: Perimeter of the shape
        """
        pass

    def get_type(self):
        """
        Return the type of shape (class name)
        :return: String with the type of shape
        """
        return self.__class__.__name__


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @round_decimals
    def get_area(self):
        return pi * self._radius ** 2

    @round_decimals
    def get_perimeter(self):
        return 2 * pi * self._radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    @round_decimals
    def get_area(self):
        semi_perimeter = (self._side1 + self._side2 + self._side3)/2
        return sqrt(semi_perimeter * (semi_perimeter - self._side1) * (semi_perimeter - self._side2) * (semi_perimeter - self._side3))

    @round_decimals
    def get_perimeter(self):
        return self._side1 + self._side2 + self._side3


class Square(Shape):
    def __init__(self, height):
        self._height = height

    @round_decimals
    def get_area(self):
        return self._height ** 2

    @round_decimals
    def get_perimeter(self):
        return 4 * self._height


class Rectangle(Shape):
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @round_decimals
    def get_area(self):
        return self._height * self._width

    @round_decimals
    def get_perimeter(self):
        return 2 * (self._height + self._width)



