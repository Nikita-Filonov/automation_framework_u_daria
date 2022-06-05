"""
Фикстуры:
 - pytest_plugins
 - indirect

Встроенные хуки/Фикстуры:
 - pytest_addoption, parser, addoption
 - request, config, getoption
 - pytest_sessionstart
 - pytest_sessionfinish
"""
import pytest


@pytest.fixture(scope='function')
def new_user(request):
    # print(f'Getting param from parametrize, "{request.param}"')
    return {
        'username': 'string',
        'email': 'some@gmail.com',
        'role': request.param
    }


class TestSome:
    @pytest.mark.parametrize('new_user', ['Student', 'Admin'], indirect=['new_user'])
    def test_some(self, new_user):
        print(new_user)

    @pytest.mark.parametrize('username', ['Student', 'Admin'])
    def test_user(self, username):
        print({
            'username': 'string',
            'email': 'some@gmail.com',
            'role': username
        })
