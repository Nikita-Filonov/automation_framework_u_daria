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

user_schema = {...} # тут схема

class User: # тут модель
    pass

# ----- Array of "user" objects -----
users = [user, user]

users_schema = {...} # тут схема


# ----- Nested "project" object -----
project = {
    'id': 1,
    'title': 'project',
    'creator': user
}

project_schema = {...} # тут схема

class Project: # тут модель
    pass
