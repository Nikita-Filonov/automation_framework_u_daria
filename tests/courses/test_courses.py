from http import HTTPStatus

import allure
import pytest
from allure_commons.types import LinkType
from jsonschema import validate

from base.api.courses import get_courses, get_course, delete_course, update_course, create_course, \
    courses_token_required, courses_send_file
from models.courses import CreateCourse, UpdateCourse, Course


# http://localhost:50853/index.html#behaviors/362548e62425745a6269d682cefebd3e/705479de203ca840/

@pytest.mark.allure_homework
@allure.severity(allure.severity_level.NORMAL)
@allure.epic('API')
@allure.feature('Courses')
@pytest.mark.courses
class TestCourses:
    schema = Course.manager.to_schema

    @allure.title('Getting all courses')
    @allure.description('В этом тесте мы получаем все курсы')
    @allure.story('Getting courses')
    @allure.issue(url='https://www.atlassian.com/software/jira', name='URGY-1025')
    @allure.link(
        url='https://www.artlebedev.ru/orfograf/',
        link_type=LinkType.TEST_CASE,
        name='Some test case'
    )
    def test_get_all_courses(self):
        get_courses_response = get_courses()
        get_courses_response_json = get_courses_response.json()
        schema = Course.manager.to_array_schema

        assert get_courses_response.status_code == HTTPStatus.OK
        validate(instance=get_courses_response_json, schema=schema)

    @allure.title('Creating course')
    @allure.description('В этом тесте мы создаем курс')
    def test_create_course_view(self):
        body = CreateCourse.manager.to_dict()

        create_course_response = create_course(body)
        create_course_response_json = create_course_response.json()

        with allure.step('Проверяем статус-код'):
            assert create_course_response.status_code == HTTPStatus.OK
        with allure.step('Проверяем title из response'):
            assert create_course_response_json['title'] == body['title']
        with allure.step('Проверяем description из response'):
            assert create_course_response_json['description'] == body['description']
        with allure.step('Проверяем image из response'):
            assert create_course_response_json['image'] == body['image']

        validate(instance=create_course_response_json, schema=self.schema)

    @allure.story('Getting courses')
    @allure.title('Getting course')
    @allure.description('В этом тесте мы получаем курс')
    def test_get_course(self, course_function):
        get_course_response = get_course(course_function['id'])
        get_course_response_json = get_course_response.json()

        with allure.step('Проверяем статус-код'):
            assert get_course_response.status_code == HTTPStatus.OK
        with allure.step('Валидируем response'):
            validate(instance=get_course_response_json, schema=self.schema)

    @allure.title('Updating course')
    @allure.description('В этом тесте мы обновляем курс')
    def test_update_course(self, course_function):
        body = UpdateCourse.manager.to_dict()

        update_course_response = update_course(course_function['id'], body)
        update_course_response_json = update_course_response.json()

        assert update_course_response.status_code == HTTPStatus.OK
        assert update_course_response_json['title'] == body['title']

        validate(instance=update_course_response_json, schema=self.schema)
        allure.attach.file('./files/hello.json', name='Some json response', attachment_type=allure.attachment_type.JSON)
        allure.attach.file('./files/hello.txt', name='Json  txt response', attachment_type=allure.attachment_type.TEXT)

    @allure.title('Deleting course')
    @allure.description('В этот тесте мы удаляем курс и проверяем, что он удален')
    def test_delete_course(self, course_function):
        deleted_course_response = delete_course(course_function['id'])

        assert deleted_course_response.status_code == HTTPStatus.NO_CONTENT
        allure.attach.file('./files/used.jpg', name='Some photo', attachment_type=allure.attachment_type.JPG)

    @allure.description('В этот тесте мы проверяем, что при вводе несуществующей почты, мы не получим токен,'
                        'с помощью которого можно получить доступ к курсу')
    @pytest.mark.parametrize('email', ['blablabla', 'abracadabra', 'daria.pishchulinana'])
    def test_courses_token_required(self, email):
        body = {
            "email": f"{email}@gmail.com"
        }
        courses_token_response = courses_token_required(body)
        courses_token_response_json = courses_token_response.json()
        assert courses_token_response.status_code == HTTPStatus.OK

        if email == 'daria.pishchulinana':
            allure.dynamic.title('Positive test')
            assert courses_token_response_json['success'] == 'yes'
        else:
            allure.dynamic.title('Negative test')
            assert courses_token_response_json['success'] == 'no'

    @allure.title('Sending file')
    @allure.description('В этот тесте мы отправляем файлы разных форматов')
    @allure.severity(allure.severity_level.MINOR)
    def test_courses_send_file(self):
        send_file_response = courses_send_file()
        send_file_response_json = send_file_response.json()

        with allure.step('Проверяем статус-код'):
            assert send_file_response.status_code == HTTPStatus.OK
        with allure.step('Проверяем название файла'):
            assert send_file_response_json['filename'] == 'hello.txt'
        with allure.step('Проверяем тип данных названия файла'):
            assert isinstance(send_file_response_json['filename'], str) # лучше порверять через json schema
