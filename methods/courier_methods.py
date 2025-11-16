import requests
import random
import string
from data import *
import json
import allure


class CourierMethods:

    def __init__(self):
        self.last_created_courier = None  

    # метод только генерирует данные курьера, НЕ создает его в системе
    @allure.step('Генерация данные курьера')
    # Не могу использовать метод staticmethod, как пишет интернет у меня проблемы с Python 3.13.9 + allure-pytest 2.15.0. 
    # пока не знаю, как решить проблему, т.к. до этого работало ((( 
    # Ошибка: ValueError: no signature found for builtin <staticmethod...>
    def generate_courier_data(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

    
        login = generate_random_string(10) + str(random.randint(1000, 9999))
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }

    @allure.step('Создание курьера')
    def post_create_courier(self, params = None):
        if params is None:
            params = self.generate_courier_data()

        self.last_created_courier = params.copy()
        response = requests.post(f'{BASE_URL}{COURIER_URL}', json = params)

        try:
            return response.json(), response.status_code    
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code


    @allure.step('Возвращение последнего созданного курьера')
    def get_last_courier_data(self):
        
        return self.last_created_courier
    

    @allure.step('Логин курьера')
    def post_login_coirier(self, params):
        response = requests.post(f'{BASE_URL}{COURIER_URL}{LOGIN_URL}', json = params)
        
        try:
            return response.json(), response.status_code    
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
    