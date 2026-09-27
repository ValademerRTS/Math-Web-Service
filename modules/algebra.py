import math


def solve_quadratic(a, b, c):
    """Решение квадратного уравнения ax² + bx + c = 0"""
    if a == 0:
        return "Ошибка: коэффициент 'a' не может быть равен нулю"

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return round(x1, 4), round(x2, 4)
    elif discriminant == 0:
        x = -b / (2 * a)
        return round(x, 4),
    else:
        return "Нет вещественных корней (D < 0)"
