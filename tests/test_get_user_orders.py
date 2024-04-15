import allure
import pytest

from http_requests.order import Order


class TestGetUserOrders:

    @pytest.mark.parametrize('authorized, expected_code', [(True, 200), (False, 401)])
    @allure.title('Тест получения заказов пользователя')
    def test_get_user_order(self, register_user, authorized, expected_code):

        token = register_user.accessToken if authorized else None

        response = Order.get_user_orders(token)

        assert response.success == authorized \
               and response.status_code == expected_code
