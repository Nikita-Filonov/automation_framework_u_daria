"""
Продолжаем знакомиться с Requests:
 - post, delete, patch, put запросы
 - Отличие data, от json
 - Работа с query params
 - Работа с headers
"""
import requests

body = {
  "title": "New lesson"
}

url = 'http://46.101.117.86/api/v1'
response_post = requests.post(url + '/lessons/', json=body)

# print(response_post.request.headers)
# print(response_post.status_code)
# print(response_post.json())

response_delete = requests.delete(url + '/lessons/', json={})
# print(response_post.status_code)
# print(response_post.json())

response_patch = requests.patch(url + '/lessons/', json=body)

response_put = requests.put(url + '/lessons/', json=body)

query_params = {
    'x': 5,
    'y': 6
}

response_get = requests.get(url + '/lessons/', params=query_params)
# print(response_get.status_code)
# print(response_get.request.url)