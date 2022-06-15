"""
Повторение:
 - pytest_addoption, parser, addoption
 - request, config, getoption
 - pytest.ini
 - Параллелизация https://pypi.org/project/pytest-xdist/

Темы:
 - Flaky тесты, https://docs.pytest.org/en/7.1.x/explanation/flaky.html#plugins
 - Requests
"""
import pytest
from random import choice


class TestUnstable:
    @pytest.mark.unstable
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_unstable(self):
        assert choice([False, 100, 200, 0])