import requests as r
import allure

from data import Url
from response_models.make_an_order_model import MakeOrder
from response_models.get_user_orders_model import UserOrders
from helpers import Validate


class Order:

    MAKE_ORDER_URL = Url.HOST_URL + 'api/orders'
    GET_USER_ORDER_URL = Url.HOST_URL + 'api/orders'

    HEADERS = {'Content-Type': 'application/json'}

    @classmethod
    @allure.step('Создание заказа')
    def create(cls, access_token=None, **kwargs):

        headers = cls.HEADERS.copy()

        if access_token:
            headers.update({'Authorization': access_token})

        response = r.post(cls.MAKE_ORDER_URL, json=kwargs, headers=headers)

        return Validate.get_model_response(MakeOrder, response)

    @classmethod
    @allure.step('Получение списка заказов')
    def get_user_orders(cls, access_token=None):

        headers = cls.HEADERS.copy()

        if access_token:
            headers.update({'Authorization': access_token})

        response = r.get(cls.GET_USER_ORDER_URL, headers=headers)

        return Validate.get_model_response(UserOrders, response)
