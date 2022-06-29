"""
1. Используя библиотеку "models-manager" и "pydantic" описать модели для сущностей

   Course - http://46.101.117.86/docs#/courses/get_courses_view_api_v1_courses__get
   CreateCourse - http://46.101.117.86/docs#/courses/create_course_view_api_v1_courses__post
   UpdateCourse - http://46.101.117.86/docs#/courses/update_course_view_api_v1_courses__course_id___patch

2. Для созданных моделей необхрдимо получить представление моделей в виде json
   MyModel (converting to json) -> {"id": 1, ...}

3. Значения полей в модели должны быть рандомизированы. Например
   MyModel (converting to json) -> {"title": "asdasdsa", ...}
   MyModel (converting to json) -> {"title": "qwereter", ...}

4. Также необходимо учесть, что некоторые поля модели могут повторяться в 
   разных моделях. Необходимо организовать структуру так, чтобы поля не повторялись.
   Сделать это можно с помощью наследования   
"""


from models_manager import Model, Field
from models_manager.utils import random_string, random_number
from pydantic import BaseModel, Field as PField

#models-manager
class Course(Model):
   title = Field(category=str, json='title', max_length=200, default=random_string)
   image = Field(category=str, json='image', max_length=100, default=random_string)
   description = Field(category=str, json='description', max_length=100, default=random_string)
   id = Field(category=int, json='id', default=random_number)
   content = Field(category=str, json='content', max_length=200, default=random_string)
   editorContent = Field(category=str, json='editorContent', default=random_string)


get_course = Course()
get_course_json = get_course.manager.to_dict()
print(f'Выводим рандомные значения первой модели в JSON (models-manager) {get_course_json}')


class CreateCourse(Course):
   class Config:
      exclude_fields = ['id', 'content', 'editorContent']


create_course = CreateCourse()
create_course_json = create_course.manager.to_dict()
print(f'Выводим рандомные значения второй модели в JSON (models-manager) {create_course_json}')


class UpdateCourse(CreateCourse):
   class Config:
      exclude_fields = ['id']

   content = Field(category=str, json='content', max_length=200, default=random_string)
   editorContent = Field(category=str, json='editorContent', default=random_string)


update_course = UpdateCourse()
update_course_json = update_course.manager.to_dict()
print(f'Выводим рандомные значения третьей модели в JSON (models-manager) {update_course_json}')


#pydantic
class PydanticCourse(BaseModel):
   title: str = PField(max_length=200, default_factory=random_string)
   image: str = PField(default_factory=random_string)
   description: str = PField(default_factory=random_string)
   id: int = PField(default_factory=random_number)
   content: str = PField(default_factory=random_string)
   editorContent: str = PField(default_factory=random_string)


get_course_1 = PydanticCourse()
get_course_1_json = get_course_1.json()
print(f'Выводим рандомные значения первой модели в JSON (pydantic) {get_course_1_json}')


class PydanticCreateCourse(PydanticCourse):
   class Config:
      fields = {'id': {'exclude': True}, 'content': {'exclude': True}, 'editorContent': {'exclude': True}}


create_course_1 = PydanticCreateCourse()
create_course_1_json = create_course_1.json()
print(f'Выводим рандомные значения второй модели в JSON (pydantic) {create_course_1_json}')


class PydanticUpdate(PydanticCourse):
   class Config:
      fields = {'id': {'exclude': True}}


update_course_1 = PydanticUpdate()
update_course_1_json = update_course_1.json()
print(f'Выводим рандомные значения третьей модели в JSON (pydantic) {update_course_1_json}')


# Better way
class CreateCourseFix(Course):
   title = Field(category=str, json='title', max_length=200, default=random_string)
   image = Field(category=str, json='image', max_length=100, default=random_string)
   description = Field(category=str, json='description', max_length=100, default=random_string)

class UpdateCourseFix(CreateCourseFix):
   content = Field(category=str, json='content', max_length=200, default=random_string)
   editorContent = Field(category=str, json='editorContent', default=random_string)

class CourseFix(UpdateCourseFix):
   id = Field(category=int, json='id', default=random_number)
