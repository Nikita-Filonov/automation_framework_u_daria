"""
1. Необходимо самостоятельно добавить два аргумента 
для командой строки при запуске тестов.

    1. Аргумент --browser - строковое значение, в котором мы указываем
       название браузера. По дефолту будет "chrome"
    2. Аргумент --screenshots_on - если аргумент указан, то значение должно 
       равняться True(boolean), если аргумент не указан, то False(boolean)

Для получения и чтения данных аргументов можно использовать фикстуры.
Данные фикстуры необходимо добавить в ``conftest.py``, который находится 
в корне проекта. То есть на каждый аргумент будет добавлена фикстура.

Также неоюходимо выбрать скоуп для фикстуры и объяснить почему.

2. В проекте используется очень много маркировок, которые не были
зарегистрированы в ``pytest.ini``. Необходимо добавить все маркировки
в проекте внутрь ``pytest.ini`` и написать к ним описание. После 
добавление маркировок, при запуске тестов не должно быть warnings

"""



