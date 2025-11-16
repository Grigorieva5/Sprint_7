import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..')) # добавляет корневую директорию проекта в путь Python 
# нужно, чтобы импортировать модули из methods/ и data.py
import pytest
from methods.order_methods import OrderMethods
import allure
from data import *


class TestCreateCourier:

    @allure.title('Получение списка заказов в зависимости от query параметров')
    @pytest.mark.parametrize("url_data", [
        ORDER_URL,
        QUERY_COURIERID,
        QUERY_NEARESTSTATION,
        QUERY_LIMIT
    ])
    def test_get_list_order_success(self, url_data):
        order_data, status_code = OrderMethods().get_orders(query=url_data)

        assert (status_code == 200 and 
                'orders' in order_data and
                isinstance(order_data['orders'], list)  and
                order_data['orders'] is not None
        )


    @allure.title('Получение ошибки несуществующего Id')
    def test_get_list_order_fails(self):
        order_data, status_code = OrderMethods().get_orders(query=QUERY_WRONG_COURIERID)

        assert (status_code == 404 and
                "Курьер с идентификатором" in order_data["message"] and
                "не найден" in order_data["message"]
        )