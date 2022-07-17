import requests
from requests import Response

from base.api.token import post_get_token
from settings import API_URL, TEST_USER

token = post_get_token(TEST_USER).json()['token']

headers = {
    "Authorization": f"Token {token}"
}


def get_courses() -> Response:
    return requests.get(f'{API_URL}/courses/', headers=headers)


def create_course(body: dict) -> Response:
    return requests.post(f'{API_URL}/courses/', json=body, headers=headers)


def get_course(course_id: int) -> Response:
    return requests.get(f'{API_URL}/courses/{course_id}', headers=headers)


def update_course(course_id: int, body: dict) -> Response:
    return requests.patch(f'{API_URL}/courses/{course_id}', json=body, headers=headers)


def delete_course(course_id: int) -> Response:
    return requests.delete(f'{API_URL}/courses/{course_id}', headers=headers)


def courses_token_required(body: dict):
    return requests.post(f'{API_URL}/courses/token-required', json=body, headers=headers)


def courses_send_file():
    with open('hello.txt', 'r') as file:
        response = requests.post(f'{API_URL}/courses/send-file', headers=headers, files={'file': file})
        return response # redundant переменная
