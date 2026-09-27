from flask import Flask, render_template, request
from modules import arifmetic, geometry, algebra

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/arifmetic', methods=['GET', 'POST'])
def arifmetic_page():
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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)