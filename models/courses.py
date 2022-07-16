from typing import Optional

from models_manager import Model, Field
from models_manager.utils import random_string


class CreateCourse(Model):
    title = Field(category=str, json='title', default=random_string)
    image = Field(category=Optional[str], json='image', default=random_string)
    description = Field(category=str, json='description', default=random_string)


class UpdateCourse(CreateCourse):
    content = Field(category=Optional[str], json='content', default=random_string)
    editor_content = Field(category=Optional[str], json='editorContent', default=random_string)


class Course(UpdateCourse):
    id = Field(category=int, json='id')