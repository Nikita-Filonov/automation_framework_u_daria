from http import HTTPStatus
from base.api.users import create_user, read_user, confirm_email
import pytest


class TestUsers():
    @pytest.mark.xfail(reason='Пользователь уже существует')
    def test_create_user(self):
        body = {
            "email": "daria.pishchulinana@gmail.com",
            "username": "DariaPishchulina",
            "password": "string"
        }
        response = create_user(body)
        response_json = response.json()

        assert response.status_code == HTTPStatus.OK
        assert response_json['email'] == body['email']
        assert response_json['username'] == body['username']


    def test_user_me(self):
        response = read_user()
        response_json = response.json()
        print(response.text)
        assert response.status_code == HTTPStatus.OK



    def test_confirm_email(self):
        body = {
            "email": "daria.pishchulinana@gmail.com",
            "code": "llPWF1XoIsQ"
        }
        response = confirm_email(body)

        assert response.status_code == HTTPStatus.OK

