# Создать класс Point, описывающий точку(атрибуты: x, y).
# Создать класс Figure.
# Создать три дочерних класса
# Circle(атрибуты: координаты центра(тип Point), радиус;
# методы: нахождение периметра и площади окружности),
# Triangle(атрибуты: три точки, методы: нахождение площади и периметра),
# Square(атрибуты: две точки, методы: нахождение площади и периметра).
# При необходимости, создавать все необходимые методы, не описанные в задании.
# Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран
# в формате: «Тип фигуры» -> «площадь».
# Примечание: в рамках задания создать два файла: classes.py и main.py.
# В первом будут описаны все классы, во втором классы будут импортированы и использованы.

from abc import ABC, abstractmethod
from typing import Union


class Point:
    """Класс описывающий точку"""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Point: ({self.x},{self.y})'


class Figure(ABC):
    """Класс, содержащий абстрактные методы,
    которые необходимо переопределить для каждого дочернего класса
    """

    @abstractmethod
    def get_perimeter(self):
        """Абстрактный метод нахождения периметра"""
        pass

    @abstractmethod
    def get_area(self):
        """Абстрактный метод нахождения площади"""
        pass


class Circle(Figure, Point):
    """Класс описывающий окружность"""

    def __init__(self, point: Point, radius: int) -> None:
        super(Point, self).__init__()
        self.point = point
        self.radius = radius

    def __str__(self) -> str:
        return f'Circle:'

    def get_perimeter(self) -> Union[int, float]:
        """Метод нахождения периметра окружности"""
        return (2 * 3.14) * self.radius

    def get_area(self) -> Union[int, float]:
        """Метод нахождения площади окружности"""
        return 3.14 * self.radius ** 2


class Triangle(Figure, Point):
    """Класс описывающий треугольник"""

    def __init__(self, point_a: Point, point_b: Point, point_c: Point) -> None:
        super(Point, self).__init__()
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.segment_length()

    def segment_length(self) -> [Union[float]]:
        """Метод нахождения длины отрезка"""
        self.len_ab = round((((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2) ** 0.5),
                            2)
        self.len_bc = round((((self.point_c.x - self.point_b.x) ** 2 + (self.point_c.y - self.point_b.y) ** 2) ** 0.5),
                            2)
        self.len_ca = round((((self.point_a.x - self.point_c.x) ** 2 + (self.point_a.y - self.point_c.y) ** 2) ** 0.5),
                            2)
        return self.len_ab, self.len_bc, self.len_ca

    def __str__(self) -> str:
        return f'Triangle:'

    def get_perimeter(self) -> [Union[float]]:
        """Метод нахождения периметра треугольника"""
        return round((self.len_ab + self.len_bc + self.len_ca), 2)

    def get_area(self) -> [Union[float]]:
        """Метод нахождения площади треугольника"""
        p = (self.get_perimeter() / 2)
        return round(((p * (p - self.len_ab) * (p - self.len_bc) * (p - self.len_ca)) ** 0.5), 2)


class Square(Triangle, Figure, Point):
    """Класс описывающий прямоугольник"""

    def __init__(self, point_a: Point, point_b: Point) -> None:
        super(Point, self).__init__()
        self.point_a = point_a
        self.point_b = point_b
        self.segment_length()

    def __str__(self) -> str:
        return f'Square:'

    def segment_length(self) -> [Union[int, float]]:
        """Метод нахождения длины отрезка"""
        self.len_ab = round((((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2) ** 0.5),
                            2)
        return self.len_ab

    def get_perimeter(self) -> [Union[int, float]]:
        """Метод нахождения периметра прямоугольника"""
        return round((self.len_ab * 4), 2)

    def get_area(self) -> [Union[int, float]]:
        """Метод нахождения площади квадрата"""
        return round((self.len_ab ** 2), 2)
