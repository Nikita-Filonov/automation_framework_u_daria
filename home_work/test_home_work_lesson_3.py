"""
1. Необходимо написать максимальное количество тестовых проверок для функций
add, minus, multiply.

Например для функции add:
    1. Складываем два числа ``add(1, 3)``
    2. Складываем две строки ``add('1', '3')``
    3. Складываем строку и число ``add(1, '3')``

В ходе выполнения негативых тестов, могут появляться ошибки и это нормально,
в будущем мы будем учиться эти ошибки тестировать

2. Необходимо сделать так, чтобы тесты можно было запустить. Для
этого возможно потребуется периеменовать файл.

3. Выбрать команду для запуска тестов
"""


def add(a: int, b: int):
    return a + b


def minus(a: int, b: int):
    return a - b


def multiply(a: int, b: int):
    return a * b


def test_add_1():
    assert add(1, 2) > 2, 'Some message'


def test_add_2():
    add(2, -3) == -1


def test_add_3():
    add(2, -3) > [2, -3]


def test_add_4():
    add('Hello ', 'world!') == 'Hello world!'


def test_add_5():
    add('2', 3) >= 23


def test_minus_1():
    minus(5, 2) == 3


def test_minus_2():
    minus(2, 3) == -1


def test_minus_3():
    assert minus('2', '-3') == 1, 'Some error happended'


def test_minus_4():
    minus(5, 6) > [-1]


def test_minus_5():
    minus(5, 6) < 3


def test_multiply_1():
    multiply(2, 3) == 6


def test_multiply_2():
    multiply(2, -3) >= -6


def test_multiply_3():
    multiply(2, 3) <= 10


def test_multiply_4():
    multiply(2, 0) == [0]


def test_multiply_5():
    multiply(4, '3') == '444'
