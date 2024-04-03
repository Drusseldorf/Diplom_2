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
    def test_change_user_data(self, register_user, new_data, authorized):

        token = register_user.accessToken if authorized else 'invalid_token'

        response = User.change(token, **new_data)

        assert response.success == authorized
