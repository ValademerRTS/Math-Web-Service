import math


# Круг
def circle_area(r):
    return round(math.pi * r ** 2, 4)


def circle_perimeter(r):
    return round(2 * math.pi * r, 4)


# Квадрат
def square_area(a):
    return a ** 2


def square_perimeter(a):
    return 4 * a


# Прямоугольник
def rectangle_area(a, b):
    return a * b


def rectangle_perimeter(a, b):
    return 2 * (a + b)


# Параллелограмм
def parallelogram_area(base, height):
    return base * height


def parallelogram_perimeter(a, b):
    return 2 * (a + b)
