from http import HTTPStatus
from jsonschema import validate
import pytest
from base.api.lessons import create_lesson, get_lesson, get_lessons
from models.lessons_schema import MyLesson


@pytest.mark.lessons
class TestLessons:
    def test_get_all_lessons(self):
        response = get_lessons()

        assert response.status_code == HTTPStatus.OK

    
    def test_create_lesson(self):
        schema = MyLesson.manager.to_schema
        body = {
          "title": "some-random-string"
        }
        create_lesson_response = create_lesson(body)
        create_lesson_json_response = create_lesson_response.json()

        get_lesson_response = get_lesson(create_lesson_json_response['id'])
        
        assert get_lesson_response.status_code == HTTPStatus.OK
        assert create_lesson_response.status_code == HTTPStatus.OK
        assert create_lesson_json_response['title'] == body['title']

        validate(instance=create_lesson_json_response, schema=schema)

    
    @pytest.mark.parametrize(
        'lesson_function', 
        ['some', 'title', 'random'], 
        indirect=['lesson_function']
    )
    def test_get_lesson(self, lesson_function):
        response = get_lesson(lesson_function['id'])
        
        assert response.status_code == HTTPStatus.OK
