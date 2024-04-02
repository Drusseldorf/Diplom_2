import pytest

from http_requests.user import User
from data import UserMessage
from helpers import Generate


class TestChangeUser:
    pass

# сохранить параметризацию. Разобраться как все же это сделать через генератор
# @pytest.mark.parametrize('new_user_data', [({'email': Generate.email()}),
#                                            ({'name': Generate.name()})])
# def test_change_user_authorized(self, register_user, new_user_data):
#
#     response = User.change(register_user.accessToken, **new_user_data)
#
#     assert response.success \
#            and response.user.email == Generate.get_last_generated_email() \
#            and response.user.name == Generate.get_last_generated_name()
