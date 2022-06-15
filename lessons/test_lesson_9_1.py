import requests
from requests import Response

url = "http://46.101.117.86/api/v1/lessons/"
response = requests.get(url)

print(response)
print(response.status_code)

lessons = response.json()
print(lessons[0], type(lessons[0]))

print(response.text, type(response.text))
print(response.content, type(response.content))