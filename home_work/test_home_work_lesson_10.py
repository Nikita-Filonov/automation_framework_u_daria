"""
Получение токена пользователя. Тренировка написания запросов к API

Для получения токена пользователя необходимо выполнить следующее:
 1. Создать пользователя, см. http://46.101.117.86/docs#/user/create_user_api_v1_user__post. 
    При создании пользователя нужно обратить внимания на email, который будет указан в теле
    запроса. Данный email должен быть действительным так, как на него придет сообщение.
 2. После создания юзера необходимо пойти на указанный email и в письме получить код подтверждения.
 3. Необохдимо подтвердить email и активировать его. Для этого нежно отправить запрос 
    http://46.101.117.86/docs#/user/confirm_email_api_v1_user_confirm_email__post
 4. После успешной активации пользователя нужно получить его token. Для этого используем
    запрос http://46.101.117.86/docs#/token/get_token_api_v1_token__post

Все действия связанные с отправкой запросов в API должны быть выполнены с использованием
библиотеки requests, кроме получение кода подтверждения, его мы получаем руками
через указанный email. 

Для понятности, рекомендую сначала выполнить все запросы через Swagger, после уже
приступить к работе через requests

Результатом выполнения задания должен быть token пользователя и код для отправки запросов
"""

import requests


url = 'http://46.101.117.86/api/v1'


body = {
    "email": "onenautm@yandex.ru",
    "username": "DariaP",
    "password": "string"
}

create_user = requests.post(url + '/user/', json=body)


body_1 = {
    "email": "onenautm@yandex.ru",
    "code": "3w2hhaMQtAiBs"
}

confirm_email = requests.post(url + '/user/send-confirm-email/', json=body_1)


body_2 = {
    "email": "onenautm@yandex.ru",
    "password": "string"
}

get_token = requests.post(url + '/token/', json=body_2)

print(get_token.text)

# последний запрос возвращает ошибку сервера 500 Internal Server Error
