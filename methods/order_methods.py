import requests
from data import *
import json
import allure


class OrderMethods:

    @allure.title('Создание заказа')
    def post_orders(self, params):
        response = requests.post(f'{BASE_URL}{ORDER_URL}', json = params)
        
        try:
            return response.json(), response.status_code    
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
        

    @allure.title('Получение списка заказаов')
    def get_orders(self, query):
        response = requests.get(f'{BASE_URL}{query}')

        try:
            return response.json(), response.status_code    
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
