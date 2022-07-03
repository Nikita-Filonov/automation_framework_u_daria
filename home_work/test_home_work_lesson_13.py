from models_manager import Model, Field
from models_manager.utils import random_string, random_number


"""
Ниже представлено несколько json объектов, необходимо 
сделать схему для каждого из них
"""

# ----- Single "user" object -----
user = {
    'id': 1,
    'username': 'say what',
    'email': 'say.what@company.com'
}

user_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'username': {'type': 'string'},
        'email': {'type': 'string'}
    },
    'required': ['id']
}
# тут схема


class User(Model):  # тут модель
    id = Field(category=int, json='id', default=random_number)
    username = Field(category=str, json='username', default=random_string, optional=True)
    email = Field(category=str, json='email', default=random_string, optional=True)


user_to_schema = User.manager.to_schema
print(f'Представляем модель User в виде jsonschema {user_to_schema}')

# ----- Array of "user" objects -----
users = [user, user]

users_schema = {
    "type": "array",
    "items": {
        'type': 'object',
        'properties': {
            'id': {'type': 'number'},
            'username': {'type': 'string'},
            'email': {'type': 'string'}
        },
        'required': ['id']
    }
}

user_to_schema = User.manager.to_array_schema

# ----- Nested "project" object -----
project = {
    'id': 1,
    'title': 'project',
    'creator': user
}

project_schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'title': {'type': 'string'},
        'creator': {
            'type': 'object',
            'properties': {
                'id': {'type': 'number'},
                'username': {'type': 'string'},
                'email': {'type': 'string'}
            },
            'required': ['id']
        }
    },
    'required': ['id', 'title']
}  # тут схема


class Project(Model):  # тут модель
    id = Field(category=int, json='id', default=random_number)
    title = Field(category=str, json='title', default=random_string)
    creator = Field(category=User, json='creator', default=user)
# в документации указан параметр related_to, но в классе Field он не прописан


project_to_schema = Project.manager.to_schema
print(f'Представляем модель Project в виде jsonschema {project_to_schema}')
