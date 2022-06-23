import pytest
import requests
from base.api.lessons import create_lesson

from settings import API_URL

@pytest.fixture(scope='function')
def lesson_function(request):
    body = {
          "title": request.param
    }
    response = create_lesson(body)
    return response.json()

@pytest.fixture(scope='class')
def lesson_class():
    body = {
          "title": "some-random-string"
    }
    response = create_lesson(body)
    return response.json()