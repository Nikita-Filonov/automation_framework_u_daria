import pytest
from base.api.courses import create_course
from models.courses import CreateCourse


@pytest.fixture(scope='function')
def course_function() -> dict:
    create_course_body = CreateCourse.manager.to_dict()
    create_course_response = create_course(create_course_body)
    return create_course_response.json()


