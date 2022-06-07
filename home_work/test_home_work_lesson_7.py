"""
1. Необходимо расширить фикстуру ``course`` так, чтобы
при запуске теста ``test_course_creation`` в конссоль печаталось

    1. Creating the course
    2. Publishing the course <- сейчас это не печатается
    3. Deleting the course

2. После выполнения задания 1, необходимо вынести фикстуру/фикстуры внутрь
``conftest`` файла. Тесты должны успешно запускаться


3. Необходимо добавить в класс несколько тестов. Количество не принципиально.
Далее необходимо добавить такую фикстуру, которая будет выполнять дейссвие при каждом
запуске теста. При этом очень важно, чтобы фикстура делала это автоматически, без
явной передачии ее внутрь теста

4. Необходимо написать фикстуру, которая будет параметризрована с помощью ``indirect``.
Задача фикстуры умножать каждый параметр теста на 2.

"""
import pytest


class TestLesson:
    def test_course_creation(self, course):
        print('Publishing the course')

    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_3(self):
        pass


# Относится к заданию 4
class TestMultiplyParam:
    @pytest.mark.parametrize('number', [2, 3, 4], indirect=['number'])  # Тут необходимо добавть несколько чисел
    def test_multiply_param(self, number):  # Тут будет передаваться твоя фикстура
        print(number)
        # Тут ожидается число ``number`` умноженное на 2
