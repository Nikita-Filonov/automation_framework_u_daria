from typing import List, Dict, Optional
from models_manager import Model, Field
from models_manager.utils import random_string, random_number

class Course(Model):
    id = Field(category=int, json='id', default=random_number, optional=True)
    title = Field(category=str, json='title', max_length=150, default=random_string)

class MyLesson(Model):
    id = Field(category=int, json='id', default=random_number, optional=True)
    title = Field(category=str, json='title', max_length=150, default=random_string)
    content = Field(category=str, json='content', min_length=1, default=random_string)
    editor_content = Field(
        category=str, 
        json='editorContent', 
        default=random_string,
    )
    courses = Field(category=Dict[str, Optional[Course]], json='courses')

print(MyLesson.manager.to_schema)

