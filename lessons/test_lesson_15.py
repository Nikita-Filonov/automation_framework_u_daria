"""
https://stackoverflow.com/questions/42897554/powershell-executionpolicy-change-bypass
https://www.netspi.com/blog/technical/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/
https://phoenixnap.com/kb/windows-set-environment-variable

iwr -useb get.scoop.sh | iex

https://pypi.org/project/allure-pytest/
pytest -m "allure" --alluredir=./allure-results
allure generate -c ./allure-results -o ./allure-report

Работа с allure:
 - Шаги - allure.step +
 - Заголовки - allure.title + 
 - Эпики - allure.epic 1 +
 - Фичи - allure.feature 2 +
 - Стори - allure.story 3 +
 - Серьезность - allure.severity +
 - Прикрепление файлов к тестам - allure.attach +
 - Описание - allure.description + 
 - Описание html - allure.description_html +
 - Прикрепление ссылок - allure.issue, allure.link +
 - Динамические модули - allure.dynamic +
"""
import pytest
import allure
from allure_commons.types import LinkType

@allure.step('Creating user with some data')
def create_user():
    pass

@pytest.mark.allure
@pytest.mark.allure_some
@allure.severity(allure.severity_level.MINOR)
@allure.epic('API')
@allure.feature('Users')
class TestAllure:
    @allure.story('Updating')
    @allure.link(
        url='https://pypi.org/project/allure-pytest/', 
        link_type=LinkType.TEST_CASE, 
        name='Some test case'
    )
    @allure.issue(url='https://pypi.org/project/allure-pytest/', name='ISSUE-1025')
    @allure.title('Test some allure report')
    @allure.description('Some test description')
    @allure.description_html('<h1>Hello from allure</h1>')
    def test_update_user(self):
        pass
    
    @allure.id('1000')
    @allure.story('Creation')
    def test_create_user(self):
        with allure.step('Connecting to database'):
            pass

        create_user()

        with allure.step('Checking status code'):
            pass

        with allure.step('Asserting user data'):
            with allure.step('Checking "username"'):
                pass

            with allure.step('Checking "email"'):
                pass 

            with allure.step('Checking token"'):
                pass
    
    def test_attach_file(self):
        allure.attach.file('./files/hello.json', name='Json response', attachment_type=allure.attachment_type.JSON)
        allure.attach.file('./files/hello.txt', name='Json response', attachment_type=allure.attachment_type.TEXT)
        allure.attach.file('./files/image.png', name='Json response', attachment_type=allure.attachment_type.PNG)
    
    @pytest.mark.parametrize('username', ['some', 1, None, 5.6])
    def test_creating_user_negative(self, username):
        allure.dynamic.title(f'Negative creation of user [{username}]')
        allure.dynamic.description(f'SOme description for {username}')