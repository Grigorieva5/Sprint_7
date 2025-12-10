import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..')) # добавляет корневую директорию проекта в путь Python 
# нужно, чтобы импортировать модули из methods/ и data.py
import pytest
from methods.courier_methods import CourierMethods
import allure
from data import *


class TestLoginCourier:

    @allure.title('Авторизация курьера')
    def test_login_courier_success(self):
        login_data, status_code = CourierMethods().post_login_coirier(params=LOGIN_COURIER)

        assert status_code == 200 and 'id' in login_data, f"Ответ содержит 'id': {login_data}"


    @allure.title('Авторизация курьера без обязательного поля')
    @pytest.mark.parametrize("invalid_data", [
        {"password": "123456789"},           
        {"login": "grigorieva"}])
    def  test_login_courier_without_mandatory_field(self, invalid_data):
        login_data, status_code = CourierMethods().post_login_coirier(params=invalid_data)
        assert status_code == 400 and "Недостаточно данных для входа" in login_data["message"]


    @allure.title('Авторизация с неверным логином')
    def test_login_courier_wrong_login(self):
        wrong_data = LOGIN_COURIER.copy()
        wrong_data["login"] = "wrong_login"
        login_data, status_code = CourierMethods().post_login_coirier(params=wrong_data)
        assert status_code == 404 and "Учетная запись не найдена" in login_data["message"]


    @allure.title('Авторизация с неверным паролем')
    def test_login_courier_wrong_password(self):
        wrong_data = LOGIN_COURIER.copy()
        wrong_data["password"] = "wrong_password"
        login_data, status_code = CourierMethods().post_login_coirier(params=wrong_data)
        assert status_code == 404 and "Учетная запись не найдена" in login_data["message"]

        
          