import requests

from http_requests.user import User
from data import UserMessage
from helpers import Generate


class TestRegisterUser:

    def test_register_unique_user(self, register_user):

        assert register_user.success \
               and register_user.status_code == requests.codes.OK

    def test_register_not_unique_email(self, register_user):

        not_unique_email = register_user.user.email

        response = User.register(email=not_unique_email, password=Generate.password(), name=Generate.name())

        assert not response.success \
               and response.message == UserMessage.ALREADY_EXISTS \
               and response.status_code == requests.codes.FORBIDDEN

    def test_register_email_missing(self):

        response = User.register(password=Generate.password(), name=Generate.name())

        assert not response.success \
               and response.message == UserMessage.MISSING_MANDATORY_FIELD \
               and response.status_code == requests.codes.FORBIDDEN
