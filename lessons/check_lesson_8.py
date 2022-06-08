"""
1. Что значит на CI?
2. Можем ли мы параллеллизировать шаги внутри теста?
"""

import pytest
from time import sleep

@pytest.mark.check
def test_hello_from_check():
    pass

@pytest.mark.check
class SuiteUser:
    def test_hello_from(self):
       pass

@pytest.mark.parallel
class TestParallel:
    def test_1(self):
        sleep(3)
        print('test_1')
    
    def test_2(self):
        sleep(5)
        print('test_2')

    def test_3(self):
        sleep(2)
        print('test_3')