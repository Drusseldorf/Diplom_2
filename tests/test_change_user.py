import allure
import pytest

from http_requests.user import User
from helpers import Generate


class TestChangeUser:

    @pytest.mark.parametrize('new_data, authorized', [
        ({'email': Generate.email()}, True),
        ({'name': Generate.name()}, True),
        ({'password': Generate.password()}, True),
        ({'email': Generate.email()}, False),
        ({'name': Generate.name()}, False),
        ({'password': Generate.password()}, False),
    ])
    @allure.title('Тест изменения данных пользователя')
    def test_change_user_data(self, register_user, new_data, authorized):
        """
        Тестирование изменения данных пользователя.

        Параметры:
            - register_user: фикстура для регистрации пользователя.
            - new_data: словарь с новыми данными пользователя.
            - authorized: флаг, указывающий, авторизован ли пользователь.

        Примечания:
            - Тест параметризован для проверки изменения различных данных пользователя как авторизованным, так и неавторизованным пользователем.
            - В случае неавторизованного пользователя, токен устанавливается в None.
            - Проверяется соответствие успешности изменения данных ожидаемому результату.
        """

        token = register_user.accessToken if authorized else None

        response = User.change(token, **new_data)

        assert response.success == authorized
