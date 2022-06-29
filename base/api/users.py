import requests
from requests import Response

from settings import API_URL


def create_user(body: dict) -> Response:
    return requests.post(f'{API_URL}/user/', json=body)


def read_user() -> Response:
    return requests.get(f'{API_URL}/user/me')


def confirm_email(body: dict) -> Response:
    return requests.post(f'{API_URL}/user/confirm-email/', json=body)