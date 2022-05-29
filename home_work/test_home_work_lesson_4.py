import pytest


@pytest.mark.markers
class TestMarkers:
    """
    Необходимо расставить маркировки так, чтобы при запуске команд ниже,
    получался соотвествующий результат:

    Input: pytest -m "markers"
    Output: 3 passed, 1 deselected, 1 warnings in 0.08s

    Input: pytest -m "regression"
    Output: 1 passed, 3 deselected, 2 warnings in 0.08s

    Input: pytest -m "regression or smoke"
    Output: 2 passed, 2 deselected, 4 warnings in 0.09s

    Input: pytest -m "regression and not feature"
    Output: 1 passed, 2 deselected, 4 warnings in 0.06s
    """

    @pytest.mark.regression
    def test_regression_mark(self):
        pass

    @pytest.mark.smoke
    def test_smoke_mark(self):
        pass

    @pytest.mark.feature
    def test_feature_mark(self):
        pass
