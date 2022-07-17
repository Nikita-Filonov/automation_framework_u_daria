
import http
from attr import field
import requests

token = "a66208bce6ac0a02eb4849b8eecbd1bc5856f31e"
url = 'http://46.101.117.86/api/v1/courses/'

headers = {
    'Authorization': f'Token {token}'
}

response = requests.get(url, headers=headers)

# print(response.status_code)
# print(response.request.headers)

# assert response.status_code == http.HTTPStatus.OK, f'Expected code 200, but get {response.status_code}'

send_file_url = 'http://46.101.117.86/api/v1/courses/send-file/'

# with open('hello.json', 'r') as file:
#    response = requests.post(send_file_url, headers=headers, files={'file': file})
#    #print(response.status_code)
#    #print(response.json())
#    #print(response.request.headers)


our_file = open('hello.json', 'w')
our_file.write('{"hello": "some_file"}')
our_file.close()

read_file = open('hello.json', 'r')
# print(read_file.readline(), type(read_file.readline()))
read_file.close()

with open('hello.json', 'w') as file:
    file.write('{"hello": "some_file"}')
