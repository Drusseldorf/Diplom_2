import pytest

from helpers import Generate
from http_requests.user import User


@pytest.fixture(scope='function')
def register_user():

    response = User.register(**Generate.full_creds())
    accessToken = response.accessToken

    yield response

    if accessToken:
        User.delete(accessToken)
