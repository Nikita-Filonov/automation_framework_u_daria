from http import HTTPStatus

import pytest
from jsonschema import validate

from base.api.courses import get_courses, get_course, delete_course, update_course, create_course, \
    courses_token_required, courses_send_file
from models.courses import CreateCourse, UpdateCourse, Course


@pytest.mark.courses
class TestCourses:
    schema = Course.manager.to_schema

    def test_get_all_courses(self):
        get_courses_response = get_courses()
        get_courses_response_json = get_courses_response.json()
        schema = Course.manager.to_array_schema

        assert get_courses_response.status_code == HTTPStatus.OK
        validate(instance=get_courses_response_json, schema=schema)

    def test_create_course_view(self):
        body = CreateCourse.manager.to_dict()

        create_course_response = create_course(body)
        create_course_response_json = create_course_response.json()

        assert create_course_response.status_code == HTTPStatus.OK
        assert create_course_response_json['title'] == body['title']
        assert create_course_response_json['description'] == body['description']
        assert create_course_response_json['image'] == body['image']

        validate(instance=create_course_response_json, schema=self.schema)

    def test_get_course(self, course_function):
        get_course_response = get_course(course_function['id'])
        get_course_response_json = get_course_response.json()

        assert get_course_response.status_code == HTTPStatus.OK

        validate(instance=get_course_response_json, schema=self.schema)

    def test_update_course(self, course_function):
        body = UpdateCourse.manager.to_dict()

        update_course_response = update_course(course_function['id'], body)
        update_course_response_json = update_course_response.json()

        assert update_course_response.status_code == HTTPStatus.OK
        assert update_course_response_json['title'] == body['title']

        validate(instance=update_course_response_json, schema=self.schema)

    def test_delete_course(self, course_function):
        deleted_course_response = delete_course(course_function['id'])

        assert deleted_course_response.status_code == HTTPStatus.NO_CONTENT

    def test_courses_token_required(self):
        body = {
            "email": "daria.pishchulinana@gmail.com"
        }
        courses_token_response = courses_token_required(body)
        courses_token_response_json = courses_token_response.json()
        print(courses_token_response.text)
        assert courses_token_response.status_code == HTTPStatus.OK
        assert courses_token_response_json['success'] == 'yes'

    def test_courses_send_file(self):
        send_file_response = courses_send_file()
        send_file_response_json = send_file_response.json()

        assert send_file_response.status_code == HTTPStatus.OK
        assert send_file_response_json['filename'] == 'hello.txt'
        assert isinstance(send_file_response_json['filename'], str)
