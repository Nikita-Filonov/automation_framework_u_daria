"""
skip
skipif
xfail
pytest -s -v -m "new_feature"
"""
import pytest


@pytest.mark.new_feature
class TestNewFeature:
    @pytest.mark.xfail(reason='New bug')
    @pytest.mark.smoke
    def test_smoke_new(self):
        raise AssertionError('New bug error!')

    @pytest.mark.regression
    def test_regression_new(self):
        pass
