import pytest


@pytest.fixture
def number(request):
    return request.param * 2


# Относится к заданию 1-3
@pytest.fixture(scope='function')
def course():
    print('Creating the course')
    yield
    # выбрала его, потому что насколько поняла - если поставить return,
    # то управление не вернется обратно в фикстуру
    print('Deleting the course')


@pytest.fixture(autouse=True)
def some_fixture():
    print('Hello, world!')
