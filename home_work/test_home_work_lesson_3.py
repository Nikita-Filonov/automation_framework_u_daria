import pytest


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
    assert add(1, 2) > 5, '3 is not more than 5'


def test_add_2():
    assert add(2, -3) == -1, '-1 is correct'


def test_add_3():
    with pytest.raises(TypeError):
        add(2, -3) > [2, -3]


def test_add_4():
    assert add('Hello ', 'world!') == 'Hello world!', 'it is not expected phrase'


def test_add_5():
    with pytest.raises(TypeError):
        add('2', 3)


def test_minus_1():
    assert minus(5, 2) == 3, 'calculating error'


def test_minus_2():
    assert minus(2, 3) == -1, 'calculating error'


def test_minus_3():
    with pytest.raises(TypeError):
        minus('2', '-3') == 1


def test_minus_4():
    with pytest.raises(TypeError):
        minus(5, 6) > [-1]


def test_minus_5():
    assert minus(5, 6) < 3, 'calculating error'


def test_multiply_1():
    assert multiply(2, 3) == 6, 'calculating error'


def test_multiply_2():
    assert multiply(2, -3) >= -6, 'calculating error'


def test_multiply_3():
    assert multiply(2, 3) <= 10, 'calculating error'


def test_multiply_4():
    assert multiply(2, 0) == [0], 'you can not compare the different data types'


def test_multiply_5():
    assert multiply(4, '3') == '444', 'multiply result does not equal expected'
