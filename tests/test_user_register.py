import allure
import pytest
import requests

from http_requests.user import User
from data import UserMessage
from helpers import Generate


class TestRegisterUser:

    @allure.title('Тест регистрации пользователя')
    def test_register_unique_user(self):

        register_user = User.register(**Generate.full_creds())

        assert register_user.success \
               and register_user.status_code == requests.codes.OK \
               and register_user.accessToken

    @allure.title('Тест регистрации пользователя с не уникальной почтой')
    def test_register_not_unique_email(self, register_user):

        not_unique_email = register_user.user.email

        response = User.register(email=not_unique_email, password=Generate.password(), name=Generate.name())

        assert not response.success \
               and response.message == UserMessage.ALREADY_EXISTS \
               and response.status_code == requests.codes.FORBIDDEN

    @pytest.mark.parametrize('creds', [
        ({'email': Generate.email(), 'password': Generate.password()}),
        ({'name': Generate.name(), 'password': Generate.password()}),
        ({'email': Generate.email(), 'name': Generate.name()})
    ])
    @allure.title('Тест регистрации пользователя с отсутствующем обязательным полем')
    def test_register_field_missing(self, creds):
        """
            Тестирование регистрации пользователя с отсутствующими обязательными полями.

            Параметры:
                - creds: словарь с данными пользователя для регистрации. Варьируются различные комбинации обязательных полей.

            Примечания:
                - Тест параметризован для различных комбинаций отсутствующих обязательных полей.
                - Проверяется ожидаемый результат регистрации: неудача, сообщение об отсутствии обязательного поля и код состояния HTTP.
        """

        response = User.register(**creds)

        assert not response.success \
               and response.message == UserMessage.MISSING_MANDATORY_FIELD \
               and response.status_code == requests.codes.FORBIDDEN
