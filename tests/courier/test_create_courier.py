import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..')) # добавляет корневую директорию проекта в путь Python 
# нужно, чтобы импортировать модули из methods/ и data.py
import pytest
from methods.courier_methods import CourierMethods
import allure


class TestCreateCourier:

    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self):
        courier_data, status_code = CourierMethods().post_create_courier()

        assert status_code == 201 and courier_data == {"ok": True}


    @allure.title('Создание двух одинаковых курьеров')
    def test_create_duplicate_courier_fails(self):
        courier_methods = CourierMethods()
        courier_methods.post_create_courier()
        last_data = courier_methods.get_last_courier_data()
        courier_data2, status_code2 = courier_methods.post_create_courier(params=last_data)
        assert status_code2 == 409 and "Этот логин уже используется" in courier_data2["message"]


    @allure.title('Создание курьера без обязательного поля')
    @pytest.mark.parametrize("invalid_data", [
        {"password": "1234", "firstName": "saske"},           
        {"login": "ninja", "firstName": "saske"}])
    def test_create_courier_without_mandatory_field(self, invalid_data):
        courier_data, status_code = CourierMethods().post_create_courier(params=invalid_data)

        assert status_code == 400 and "Недостаточно данных для создания учетной записи" in courier_data["message"]


    @allure.title('Создание курьера только с обязательными поля')
    def test_create_courier_without_optional_field(self):
        courier_methods = CourierMethods()  
        params = courier_methods.generate_courier_data()
        params.pop("firstName", None)
        courier_data, status_code = CourierMethods().post_create_courier(params=params)
        assert status_code == 201 and courier_data == {"ok": True}


