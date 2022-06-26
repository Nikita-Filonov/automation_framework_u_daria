"""
json object => python class

{"id": 1, "title": "string"} => class Model:
                                    id: int = 1
                                    title: str = "string"

✅              
⛔                      
"""
from dataclasses import dataclass
from models_manager import Model, Field
from models_manager.utils import random_string, random_number
from pydantic import BaseModel, Field as PField

lesson = {
    "title": "Some Title", # string
    "id": 0, # number
    "content": "Some Content", # string
    "editorContent": "Some Editor Content" # string
}

create_lesson = {
    "title": "string" # string
}

# dataclasses
@dataclass
class Lesson:
    id: int
    title: str
    content: str
    editorContent: str

lesson = Lesson(id=5, title='sddfds', content='saddsf', editorContent='adsfd')
lesson
lesson.id
lesson.title


def create_lesson(data: Lesson):
    data.id
    data.title

# models-manager
class CreateModelsManagerLesson(Model):
    title = Field(category=str, json='title', max_length=100, default=random_string)
    content = Field(category=str, json='content', default=random_string)
    editor_content = Field(category=str, json='editorContent', default=random_string)

class ModelsManagerLesson(CreateModelsManagerLesson):
    id = Field(category=int, json='id', default=random_number)

lesson = ModelsManagerLesson(id=5, title='sddfds', content='saddsf', editorContent='adsfd')
lesson
lesson.id.value
lesson.title.value

def create_lesson_1(data: ModelsManagerLesson):
    data.id
    data.title
    data.editor_content


lesson.manager.to_dict(json_key=True), type(lesson.manager.to_dict())
lesson.manager.to_dump(), type(lesson.manager.to_dump())
lesson.manager.to_dict_with_negative_max_length(fields=[ModelsManagerLesson.title])
lesson.manager.to_dict_with_empty_string_fields(fields=[ModelsManagerLesson.title, ModelsManagerLesson.id])

lesson.manager.to_schema

ModelsManagerLesson.manager.to_dict()

# pydantic
class PydanticLesson(BaseModel):
    id: int = PField(default_factory=random_number)
    title: str = PField(max_length=100, default_factory=random_string)
    content: str = PField(default_factory=random_string)
    editor_content: str = PField(alias='editorContent', default_factory=random_string)

lesson = PydanticLesson(id=5, title='sddfds', content='saddsf', editorContent='adsfd')
print(lesson.id)
print(lesson.title)
print(lesson)

print(lesson.dict(by_alias=True))
print(lesson.json())

PydanticLesson.schema()
print(PydanticLesson().dict())