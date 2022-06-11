import pytest

pytest_plugins = [
    'utils.fixtures.users'
]


def pytest_sessionstart():
    print('Health checking our server')
    print('Making migrations')
    print('Making seeding')


def pytest_sessionfinish():
    print('\nClearing the database')


@pytest.fixture(scope="session")
# один сервер на одну сессию, мне кажется это вполне логичным
def domain(request):
    return request.config.getoption("--domain")

@pytest.fixture(scope="session")
# знать бы, как работают порты....
def port(request):
    return request.config.getoption("--port")

@pytest.fixture(scope="session")
# на самом деле не знаю, какой скоуп тут подойдет
def log(request):
    return request.config.getoption("--save-log")

@pytest.fixture(scope="module")
# предполагаю, что UI тесты могут лежать например в каком-то определенном модуле, и для них
# было бы логично выбирать браузер
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="function")
# скриншоты нужны для конкретных тестов
def screenshots(request):
    return request.config.getoption("--screenshots_on")


def pytest_addoption(parser):
    parser.addoption("--domain", default="dev", help="Please provide the domain", action="store")
    parser.addoption("--port", default="8000", help="Please provide the port", action="store")
    parser.addoption("--save-log", help="Save log?", action="store_true")
    parser.addoption("--browser", default="chrome", help="Please provide the browser", action="store")
    parser.addoption("--screenshots_on", help="Make screenshots?", action="store_true")

