"""Главный модуль Flask веб-калькулятора."""

from flask import Flask, render_template, request
from modules import arifmetic, geometry, algebra

app = Flask(__name__)


@app.route('/')
def index():
    """
    Отображает главную страницу веб-калькулятора.

    Возвращаемое значение:
        str: HTML-шаблон index.html.
    """
    return render_template('index.html')


@app.route('/arifmetic', methods=['GET', 'POST'])
def arifmetic_page():
    """
    Обрабатывает GET и POST запросы для раздела арифметических операций.

    Возвращаемое значение:
        str: HTML-страница с результатом вычислений или формой ввода.
    """
    result = None
    if request.method == 'POST':
        try:
            a, b = float(request.form['a']), float(request.form['b'])
            op = request.form['operation']
            if op == 'add':
                result = arifmetic.add(a, b)
            elif op == 'subtract':
                result = arifmetic.subtract(a, b)
            elif op == 'multiply':
                result = arifmetic.multiply(a, b)
            elif op == 'divide':
                result = arifmetic.divide(a, b)
            elif op == 'power':
                result = arifmetic.power(a, b)
        except ValueError:
            result = "Ошибка: введите числа"
    return render_template('index.html', section='arifmetic', result=result)


@app.route('/geometry', methods=['GET', 'POST'])
def geometry_page():
    """
    Обрабатывает GET и POST запросы для раздела геометрических вычислений.

    Возвращаемое значение:
        str: HTML-страница с результатами расчета площади/периметра.
    """
    result = None
    if request.method == 'POST':
        try:
            fig = request.form.get('figure')
            calc = request.form.get('calc')

            if fig == 'circle':
                r = float(request.form.get('r', 0))
                result = geometry.circle_area(r) if calc == 'area' else geometry.circle_perimeter(r)
            elif fig == 'square':
                a = float(request.form.get('a', 0))
                result = geometry.square_area(a) if calc == 'area' else geometry.square_perimeter(a)
            elif fig == 'rectangle':
                a = float(request.form.get('a', 0))
                b = float(request.form.get('b', 0))
                result = geometry.rectangle_area(a, b) if calc == 'area' else geometry.rectangle_perimeter(a, b)
            elif fig == 'parallelogram':
                a = float(request.form.get('a', 0))
                b = float(request.form.get('b', 0))
                result = geometry.parallelogram_area(a, b) if calc == 'area' else geometry.parallelogram_perimeter(a, b)
        except ValueError:
            result = "Ошибка: неверные входные данные"
    return render_template('index.html', section='geometry', result=result)


@app.route('/algebra', methods=['GET', 'POST'])
def algebra_page():
    """
    Обрабатывает GET и POST запросы для решения квадратных уравнений.

    Возвращаемое значение:
        str: HTML-страница с найденными корнями или сообщением об ошибке.
    """
    result = None
    if request.method == 'POST':
        try:
            a = float(request.form.get('a', 0))
            b = float(request.form.get('b', 0))
            c = float(request.form.get('c', 0))
            result = algebra.solve_quadratic(a, b, c)
        except ValueError:
            result = "Ошибка: введите числовые коэффициенты"
    return render_template('index.html', section='algebra', result=result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)