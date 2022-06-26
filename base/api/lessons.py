import requests
from requests import Response

from settings import API_URL


def get_lessons() -> Response:
    return requests.get(f'{API_URL}/lessons/')


def create_lesson(body: dict) -> Response:
    """
    body = {'id': 1 ...}
    """
    return requests.post(f'{API_URL}/lessons/', json=body)


def get_lesson(lesson_id: int) -> Response:
    return requests.get(f'{API_URL}/lessons/{lesson_id}')