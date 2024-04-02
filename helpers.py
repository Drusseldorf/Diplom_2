from faker import Faker
from pydantic import ValidationError


class Generate:

    last_generated_password = None
    last_generated_email = None
    last_generated_name = None

    @classmethod
    def name(cls):
        cls.last_generated_name = Faker().name()
        return cls.last_generated_name

    @classmethod
    def full_creds(cls):
        return {
            'email': cls.email(),
            'password': cls.password(),
            'name': cls.name()
        }

    @classmethod
    def email(cls):
        cls.last_generated_email = Faker().email()
        return cls.last_generated_email

    @classmethod
    def password(cls):
        cls.last_generated_password = Faker().password()
        return cls.last_generated_password

    @classmethod
    def get_last_generated_password(cls):
        return cls.last_generated_password

    @classmethod
    def get_last_generated_email(cls):
        return cls.last_generated_email

    @classmethod
    def get_last_generated_name(cls):
        return cls.last_generated_name


class Validate:

    @staticmethod
    def get_model_response(model, response):

        try:
            response_model = model.model_validate({
                **response.json(),
                "status_code": response.status_code
            })
        except ValidationError as e:
            response_model = model(success=False, message=e.json(), status_code=response.status_code)
        except ValueError as e:
            response_model = model(success=False, message=str(e), status_code=response.status_code)

        return response_model
