from pydantic import ValidationError
import requests as r

from data import Url
from response_models.register_user_model import RegisterUser


class User:
    REGISTER_URL = Url.HOST_URL + 'api/auth/register'
    DELETE_URL = Url.HOST_URL + 'api/auth/user'

    HEADERS = {'Content-Type': 'application/json'}

    @classmethod
    def register(cls, **kwargs):

        response = r.post(cls.REGISTER_URL, json=kwargs, headers=cls.HEADERS)

        try:
            response_model = RegisterUser.model_validate_json(response.text)
        except ValidationError as e:
            response_model = RegisterUser(success=False, message=e.json())
        except ValueError as e:
            response_model = RegisterUser(success=False, message=str(e))

        return response_model

    @classmethod
    def delete(cls, accessToken):

        headers = {'Authorization': accessToken}

        response = r.delete(cls.DELETE_URL, headers=headers)

        return response
