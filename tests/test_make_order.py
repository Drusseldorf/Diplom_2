import allure
import pytest
import requests

from http_requests.order import Order
from data import OrderFields


class TestMakeOrder:

    @pytest.mark.parametrize('ingredients, authorized, expected_result, expected_code', [
        (OrderFields.INGREDIENTS, True, True, 200),
        ({}, True, False, 400),
        (OrderFields.INGREDIENTS, False, True, 200),
        ({}, False, False, 400)
    ])
    @allure.title('Тест создания заказа')
    def test_make_order(self, register_user, ingredients, authorized, expected_result, expected_code):
        """
                Тестирование создания заказа при различных переданных данных

                Параметры:
                    - register_user: фикстура для регистрации пользователя.
                    - ingredients: словарь с ингредиентами заказа.
                    - authorized: флаг, указывающий, авторизован ли пользователь.
                    - expected_result: ожидаемый результат создания заказа (успех или неудача).
                    - expected_code: ожидаемый HTTP-код ответа.

                Примечания:
                    - Тесты параметризованы для различных вариантов входных данных: с ингредиентами и без, с авторизацией и без.
                    - В случае неавторизованного пользователя, токен устанавливается в None.
                    - Проверяется успешность создания заказа и соответствие HTTP-кода ожидаемому.
        """

        token = register_user.accessToken if authorized else None

        response = Order.create(token, **ingredients)

        assert response.success == expected_result and response.status_code == expected_code

    @allure.title('Тест создания заказа с некорректным номером ингредиента')
    def test_invalid_ingredient_make_order(self):

        response = Order.create(**OrderFields.WRONG_INGREDIENT)

        assert not response.success \
               and response.status_code == requests.codes.INTERNAL_SERVER_ERROR
