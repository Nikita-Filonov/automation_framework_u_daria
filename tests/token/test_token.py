from http import HTTPStatus
from base.api.token import post_get_token


class TestToken:
    def test_get_token(self):
        body = {
            "email": "daria.pishchulinana@gmail.com",
            "password": "string"
        }
        expected_token = {"token":"500356b93224309d1345a5c01292bddd618e199c"}
        response = post_get_token(body)

        assert response.status_code == HTTPStatus.OK
        assert response.json() == expected_token
