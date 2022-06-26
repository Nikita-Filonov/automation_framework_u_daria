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

class Course:
   pass