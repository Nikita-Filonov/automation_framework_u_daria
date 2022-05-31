"""
- Повторение параметризации
- Параметризация нескольки аргументов
- Параметризация для классов
- Параметризация рвзных вариаций
- Кастомные id для параметризации
- Динамические маркировки для параметризации
"""
import pytest


@pytest.mark.smoke
@pytest.mark.parametrize(
    'username, email',
    [
        ['string', 'string@gmail.com'],
        ['string12345', 'string@gmail.com'],
        [None, None],
    ]
)
def test_user_creation0(username, email):
    print(f'username is: {username} and email is {email}')


class TestUser:

    def test_user_creation(self):
        pass

    @pytest.mark.parametrize(
        'username',
        ['string', 1, None, 'too_long_username'],
        ids=lambda param: f'Our current param is {param}'
    )
    def test_user_updating(self, username):
        print(username)


@pytest.mark.parametrize(
    'username',
    [
        pytest.param('string', id='Some string param', marks=pytest.mark.xfail(reason='Here is new bug')),
        pytest.param(1, marks=pytest.mark.skip(reason='Some reason')),
        None
    ]
)
def test_user_creation(username):
    pass
