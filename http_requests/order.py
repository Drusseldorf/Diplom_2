import requests as r

from data import Url
from response_models.make_an_order_model import MakeOrder
from helpers import Validate


class Order:

    MAKE_ORDER_URL = Url.HOST_URL + 'api/orders'

    HEADERS = {'Content-Type': 'application/json'}

    @classmethod
    def create(cls, access_token=None, **kwargs):

        headers = cls.HEADERS.copy()

        if access_token:
            headers.update({'Authorization': access_token})

        response = r.post(cls.MAKE_ORDER_URL, json=kwargs, headers=headers)

        return Validate.get_model_response(MakeOrder, response)
