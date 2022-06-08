"""
Повторение:
 - pytest_plugins
 - indirect
 - pytest_sessionstart
 - pytest_sessionfinish

Встроенные хуки/Фикстуры:
 - pytest_addoption, parser, addoption
 - request, config, getoption
 - pytest.ini
 - Параллелизация
"""
import pytest


@pytest.mark.lesson_8
class TestSome:
    def test_some(self, request, domain):
        print('Test some', f'https://{domain}.my.comapny/api/')
        
        port = request.config.getoption('--port')
        print(type(port))

        save_log = request.config.getoption('--save-log')
        print(save_log, type(save_log))