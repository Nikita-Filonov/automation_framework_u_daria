"""
- Повторение параметризации
- Фиксутры, conftest
- Скоупы:
  - session
  - package
  - module
  - class
  - function
- autouse
- indirect
- plugins
"""


class TestUser:
    def test_get_user(self, user, user_with_password):
        print('Getting the user')

    def test_update_user(self, user, user_with_password):
        print('Updating the user')
