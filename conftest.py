import pytest

from helpers import Generate
from http_requests.user import User


@pytest.fixture(scope='function')
def register_user():

    response = User.register(email=Generate.email(), password=Generate.password(), name=Generate.name())
    accessToken = response.accessToken if hasattr(response, 'accessToken') else None

    yield response

    if accessToken:
        User.delete(accessToken)
