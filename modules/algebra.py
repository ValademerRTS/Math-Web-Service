"""Модуль алгебраических вычислений."""

import math


def solve_quadratic(a: float, b: float, c: float):
    """
    Решает квадратное уравнение вида ax² + bx + c = 0.

    Параметры:
        a (float): Старший коэффициент (a ≠ 0).
        b (float): Второй коэффициент.
        c (float): Свободный член.

    Возвращаемое значение:
        tuple | str: Кортеж с корнями уравнения (один или два) или строка с описанием ошибки.

    Пример вызова:
        >>> solve_quadratic(1, -5, 6)
        (3.0, 2.0)
        >>> solve_quadratic(1, -2, 1)
        (1.0,)
        >>> solve_quadratic(1, 0, 1)
        'Нет вещественных корней (D < 0)'
        >>> solve_quadratic(0, 2, 1)
        "Ошибка: коэффициент 'a' не может быть равен нулю"
    """
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