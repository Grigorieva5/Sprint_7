import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..')) # добавляет корневую директорию проекта в путь Python 
# нужно, чтобы импортировать модули из methods/ и data.py
import pytest
from methods.order_methods import OrderMethods
import allure
from data import *


class TestCreateOrders:

    @allure.title('Успешное создание заказа с разными значениями color')
    @pytest.mark.parametrize("color_value", [
        (["BLACK"]),
        (["GREY"]), 
        (["BLACK", "GREY"]),
        ([]),
        (None)
    ])
    def test_create_order_success(self, color_value):
        params = CREATE_ORDER.copy()
        if color_value is None:
            params.pop("color", None)
        else:
            params["color"] = color_value
        order_data, status_code = OrderMethods().post_orders(params=params)

        assert status_code == 201 and 'track' in order_data, f"Ответ содержит 'track': {order_data}"

  