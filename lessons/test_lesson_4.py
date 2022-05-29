"""
Темы:

1. Повторение маркировок
2. Проверки
3. Параметризация
"""
import pytest


def get_user_by_id(user_id: int):
    raise NotImplementedError(f'Can not found user with id={user_id}')


@pytest.mark.some
def test_some():
    actual_response_body = {'id': 1, 'username': 'some'}
    expected_response_body = {'id': 2, 'username': 'some'}
    assert actual_response_body == expected_response_body


@pytest.mark.other
def test_other():
    with pytest.raises(ArithmeticError):
        get_user_by_id(user_id=5)


def create_user(user_payload: dict):
    pass


@pytest.mark.smoke
@pytest.mark.parametrize(
    'username',
    [
        'string',
        1,
        None,
        'stringstringstringstringstringstringstring'
    ]
)
def test_user_creation0(username):
    user_data = {'id': 1, 'email': username}
    print(f'Creating user with data {user_data}')
    create_user(user_data)


@pytest.mark.smoke
@pytest.mark.parametrize(
    'user_data',
    [
        {'id': 1, 'email': 'string'},
        {'id': 2, 'email': 1},
        {'id': 3, 'email': None},
        {'id': 4, 'email': 'stringstringstringstringstringstringstring'},
    ]
)
def test_user_creation(user_data):
    print(f'Creating user with data {user_data}')
    create_user(user_data)
