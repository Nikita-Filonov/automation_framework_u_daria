"""
1. У нас есть нестабильный тест, который может 
   иногда падать. Необходимо добавить такую маркировку, 
   при которой тест будет перезапущен 5 раз с периодичностью в 1 секунду

2. Необходимо запустить тесты ниже используя несколько видов команд

   1. pytest -m "threading_1 or threading_2"
   2. pytest -m "threading_1 or threading_2" -n 2 --dist load
   3. pytest -m "threading_1 or threading_2" -n 2 --dist loadscope

   При этом после каждого запуска необходимо записать время выполнения тестов.
   Например: 
   == 4 passed, 22 warnings in <some_time_here>s ==

   После запуска всех команд и получения результатов, необходимо ответить на вопрос.
   Тесты какой из команд будут выполнены быстрее всего и почему?
"""
import random
from time import sleep

import pytest


# задание 1
def test_some_unstable_feature():
    assert random.choice([True, False, '', 0])

# задание 2
@pytest.mark.threading_1
class TestThreading1:
    def test_1(self):
        sleep(10)

    def test_2(self):
        sleep(5)

@pytest.mark.threading_2
class TestTreading2:
    def test_3(self):
        sleep(2)

    def test_4(self):
        sleep(3)
