from pydantic import ValidationError
import requests as r
import json

from data import Url
from response_models.register_user_model import RegisterUserSuccess, RegisterUserFail


class User:
    REGISTER_URL = Url.HOST_URL + 'api/auth/register'
    DELETE_URL = Url.HOST_URL + 'api/auth/user'

    HEADERS = {'Content-Type': 'application/json'}

    @classmethod
    def register(cls, **kwargs):

        data = json.dumps({key: value for key, value in kwargs.items()})
        response = r.post(cls.REGISTER_URL, data, headers=cls.HEADERS)

        try:
            response_model = RegisterUserSuccess.model_validate_json(response.text)
        except ValidationError:
            response_model = RegisterUserFail.model_validate_json(response.text)

        return response_model

    @classmethod
    def delete(cls, accessToken):

        headers = {'Authorization': accessToken}

        response = r.delete(cls.DELETE_URL, headers=headers)

        return response
