from typing import Dict, Union, Optional, List, Literal, Tuple
from jsonschema import validate
from models_manager import Model, Field
from models_manager.utils import random_string, random_number

json = {
  "title": "string",
  "id": 0,
  "content": "string",
  "editorContent": "string",
  "editorContent2": "string"
}

schema = {
  "type": "array",
  "items": {
    "title": "Lesson",
    "type": "object",
    "properties": {
      "title": { "maxLength": 100, "type": "string" },
      "content": { "type": "string" },
      "editorContent": { "type": "string" },
      "id": { "type": "number" }
    },
    "required": ["title", "content", "editorContent", "id"],
    "additionalProperties": False
  },
}

validate(instance=[json], schema=schema)

class MyLesson(Model):
    id = Field(category=int, json='id', default=random_number, optional=True)
    title = Field(category=str, json='title', max_length=150, default=random_string)
    content = Field(category=str, json='content', min_length=1, default=random_string)
    editor_content = Field(
        category=int, 
        json='editorContent', 
        default=random_number,
        gt=5,
        le=10
    )

# print(MyLesson.manager.to_schema)
print(MyLesson.manager.to_array_schema)

# typing
json_int = {'a': 1, 'b': 2, 'c': 3}
dict # {}, {1:2}, {True: 1}
Dict[str, int]

json_int_str = {'a': 1, 'b': 'bbbbbb', 'c': 3}
Dict[str, Union[int, str]]


json_int_none = {'a': 1, 'b': None, 'c': 3}
Dict[str, Optional[int]] # Union[int, None]


array_json = [json_int] # list
List[Dict[str, int]]

status: Literal["active", "disabled", "pending"] = "active" or "disabled" or "pending"
Literal["active", "disabled", "pending"]


tuple_json = (1, 'some', True)
Tuple[int, str, bool]


class SomeLesson(Model):
    id = Field(category=int, json='id', default=random_number, optional=True)
    title = Field(category=Union[str, int, bool], json='title', max_length=150, default=random_string)

print(SomeLesson.manager.to_schema)    

schema_lesson = {
    'title': 'SomeLesson', 
    'type': 'object', 
    'properties': {
        'id': {'type': 'number'}, 
        'title': {
            'maxLength': 150,
             'anyOf': [{'type': 'string'}, {'type': 'number'}, {'type': 'boolean'}]
        }
    },
    'required': ['title']
}