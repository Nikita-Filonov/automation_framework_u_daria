import pytest

pytest_plugins = [
    'utils.fixtures.users'
]


def pytest_sessionstart():
    print('Health checking our server')
    print('Making migrations')
    print('Making seeding')


def pytest_sessionfinish():
    print('Clearing the database')


@pytest.fixture(scope="session")
def domain(request):
    return request.config.getoption("--domain")


def pytest_addoption(parser):
    parser.addoption("--domain", default="dev", help="Please provide the domain", action="store")
    parser.addoption("--port", default="8000", help="Please provide the port", action="store")
    parser.addoption("--save-log", help="Save log?", action="store_true")

