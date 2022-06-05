pytest_plugins = [
    'utils.fixtures.users'
]


def pytest_sessionstart():
    print('Health checking our server')
    print('Making migrations')
    print('Making seeding')


def pytest_sessionfinish():
    print('Clearing the database')
