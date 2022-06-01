import pytest


@pytest.fixture(scope='function')
def user():
    print('Creating the user')
    yield
    print('Deleting the user')
