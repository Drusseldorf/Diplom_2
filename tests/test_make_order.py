import pytest
import requests

from http_requests.order import Order
from data import OrderFields


class TestMakeOrder:

    @pytest.mark.parametrize('ingredients, authorized, expected_result', [
        (OrderFields.INGREDIENTS, True, True),
        ({}, True, False),
        (OrderFields.INGREDIENTS, False, True),
        ({}, False, False)
    ])
    def test_make_order(self, register_user, ingredients, authorized, expected_result):

        token = register_user.accessToken if authorized else 'invalid_token'

        response = Order.create(token, **ingredients)

        assert response.success == expected_result

    def test_invalid_ingredient_make_order(self):

        response = Order.create(**OrderFields.WRONG_INGREDIENT)

        print(response)

        assert not response.success \
               and response.status_code == requests.codes.INTERNAL_SERVER_ERROR
