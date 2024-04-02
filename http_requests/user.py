import requests as r

from data import Url
from helpers import Validate
from response_models.register_user_model import RegisterUser
from response_models.login_user_model import LoginUser
from response_models.change_user_model import ChangeUser


class User:

    REGISTER_URL = Url.HOST_URL + 'api/auth/register'
    LOGIN_URL = Url.HOST_URL + 'api/auth/login'
    CHANGE_USER_DATA_URL = Url.HOST_URL + 'api/auth/user'
    DELETE_URL = Url.HOST_URL + 'api/auth/user'

    HEADERS = {'Content-Type': 'application/json'}

    @classmethod
    def register(cls, **kwargs):

        response = r.post(cls.REGISTER_URL, json=kwargs, headers=cls.HEADERS)

        return Validate.get_model_response(RegisterUser, response)

    @classmethod
    def login(cls, **kwargs):

        response = r.post(cls.LOGIN_URL, json=kwargs, headers=cls.HEADERS)

        return Validate.get_model_response(LoginUser, response)

    @classmethod
    def change(cls, accessToken, **kwargs):

        headers = {'Authorization': accessToken}

        response = r.patch(cls.CHANGE_USER_DATA_URL, json=kwargs, headers=headers)

        return Validate.get_model_response(ChangeUser, response)

    @classmethod
    def delete(cls, accessToken):

        headers = {'Authorization': accessToken}

        response = r.delete(cls.DELETE_URL, headers=headers)

        return response
