from faker import Faker
from pydantic import ValidationError
import json


class Generate:

    last_generated_password = None

    @classmethod
    def full_creds(cls):
        return {
            'email': cls.email(),
            'password': cls.password(),
            'name': cls.name()
        }

    @staticmethod
    def name(cls):
        return Faker().name()

    @staticmethod
    def email(cls):
        return Faker().email()

    @classmethod
    def password(cls):
        cls.last_generated_password = Faker().password()
        return cls.last_generated_password

    @classmethod
    def get_last_generated_password(cls):
        return cls.last_generated_password


class Validate:

    @staticmethod
    def get_model_response(model, response):
        try:
            response_model = model.model_validate({
                **response.json(),
                "status_code": response.status_code
            })
        except ValidationError as e:
            response_model = model(success=False, message=f'Validation Error: {str(e)}', status_code=response.status_code)
        except json.JSONDecodeError:
            response_model = model(success=False, message=f'Not a valid JSON: {response.text}', status_code=response.status_code)

        return response_model
