import requests
from requests import Response

from settings import API_URL


def post_get_token(body: dict) -> Response:
    return requests.post(f'{API_URL}/token/', json=body)