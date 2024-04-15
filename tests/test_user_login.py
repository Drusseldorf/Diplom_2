import allure
import requests

from http_requests.user import User
from data import UserMessage
from helpers import Generate


class TestUserLogin:

    @allure.title('Тест логина пользователя')
    def test_login_existing_user(self, register_user):

        email = register_user.user.email
        password = Generate.get_last_generated_password()

        response = User.login(email=email, password=password)

        assert response.success \
               and response.status_code == requests.codes.OK \
               and response.accessToken

    @allure.title('Тест логина пользователя с неверным паролем')
    def test_login_with_wrong_password(self, register_user):

        email = register_user.user.email
        wrong_password = Generate.password()

        response = User.login(email=email, password=wrong_password)

        assert not response.success \
               and response.status_code == requests.codes.UNAUTHORIZED \
               and response.message == UserMessage.WRONG_CREDS

    @allure.title('Тест логина пользователя с неверным логином')
    def test_login_with_wrong_email(self, register_user):

        wrong_email = Generate.email()
        password = Generate.get_last_generated_password()

        response = User.login(email=wrong_email, password=password)

        assert not response.success \
               and response.status_code == requests.codes.UNAUTHORIZED \
               and response.message == UserMessage.WRONG_CREDS
