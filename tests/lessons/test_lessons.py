from http import HTTPStatus

import pytest
from base.api.lessons import create_lesson, get_lesson, get_lessons


@pytest.mark.lessons
class TestLessons:
    def test_get_all_lessons(self):
        response = get_lessons()

        assert response.status_code == HTTPStatus.OK

    
    def test_create_lesson(self):
        body = {
          "title": "some-random-string"
        }
        create_lesson_response = create_lesson(body)
        create_lesson_json_response = create_lesson_response.json()

        get_lesson_response = get_lesson(create_lesson_json_response['id'])
        
        assert get_lesson_response.status_code == HTTPStatus.OK
        assert create_lesson_response.status_code == HTTPStatus.OK
        assert create_lesson_json_response['title'] == body['title']

    
    @pytest.mark.parametrize(
        'lesson_function', 
        ['some', 'title', 'random'], 
        indirect=['lesson_function']
    )
    def test_get_lesson(self, lesson_function):
        response = get_lesson(lesson_function['id'])
        
        assert response.status_code == HTTPStatus.OK
