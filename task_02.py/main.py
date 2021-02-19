from classes2 import *


point_a = Point(1, 2)
print(point_a)
circle = Circle(point_a, 7)
print(circle)
print('Площадь круга:', circle.get_area(), 'Периметр круга', circle.get_perimeter())
print('-' * 10)

point_b = Point(2, 5)
point_c = Point(5, 4)
print(point_a, point_b)
triangle = Triangle(point_a, point_b, point_c)
print(triangle)

print('катет ав:', triangle.len_ab)
print('катет bc:', triangle.len_bc)
print('катет ca:', triangle.len_ca)
print('периметр треугольника:', triangle.get_perimeter(), 'площадь треугольника:', triangle.get_area())
print('-' * 10)

square = Square(point_a, point_b)
print(point_a, point_b)
print(square)
print('сторона квадрата:', square.len_ab)
print('периметр квадрата:', square.get_perimeter(), 'площадь квадрата:', square.get_area())
print('-' * 10)

figures = [circle, triangle, square]
for figure in figures:
    print(figure, ' -> area: ', figure.get_area())

