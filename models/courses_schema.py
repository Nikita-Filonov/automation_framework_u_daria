from models_manager import Model, Field
from models_manager.utils import random_string, random_number


class CoursesSchema(Model):
    title = Field(category=str, json='title', max_length=150, default=random_string)
    image = Field(category=str, json='image', default=random_string)
    description = Field(category=str, json='description', default=random_string)
    id = Field(category=int, json='id', default=random_number, optional=True)
    content = Field(category=str, json='content', min_length=1, default=random_string)
    editor_content = Field(
        category=int,
        json='editorContent',
        default=random_number,
        gt=5,
        le=10
    )
