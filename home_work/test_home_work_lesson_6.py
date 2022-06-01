"""
Необходимо написать 4 вида фикстур
1. Фикстура со scope='function'
2. Фикстура со scope='class'
3. Фикстура со scope='module'
4. Фикстура со scope='session'

При запуске тестов должно быть выведено. Фикстуры можно писать
в этом же файле. Для примера уже создана одна фикстура "function".
Названия фикстур могут быть любые

1. Hello from, function fixture - 6 раз
2. Hello from, class fixture - 2 раза
3. Hello from, module fixture - 1 раз
4. Hello from, session fixture - 1 раз

Note:
    Запустить тесты в файле "test_home_work_lesson_6.py" можно командой
    > pytest -s -v home_work/test_home_work_lesson_6.py
"""

import pytest


@pytest.fixture(scope='function')
def function():
    ...


class TestFixtures:
    def test_feature_1(self, function):
        pass

    def test_feature_2(self):
        pass

    def test_feature_3(self):
        pass


class TestFixtures2:
    def test_feature_4(self):
        pass

    def test_feature_5(self):
        pass

    def test_feature_6(self):
        pass
