from http_requests.user import User
from data import UserMessage
from helpers import Generate


class TestRegisterUser:

    def test_register_unique_user(self, register_user):

        assert register_user.success

    def test_register_not_unique_email(self, register_user):

        not_unique_email = register_user.user.email

        response = User.register(email=not_unique_email, password=Generate.password(), name=Generate.name())

        assert not response.success and response.message == UserMessage.ALREADY_EXISTS

    def test_register_email_missing(self):

        response = User.register(password=Generate.password(), name=Generate.name())

        assert not response.success and response.message == UserMessage.MISSING_MANDATORY_FIELD
