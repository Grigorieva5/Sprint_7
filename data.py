BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
COURIER_URL = 'courier/'
LOGIN_URL = 'login/'
ORDER_URL = 'orders/'

LOGIN_COURIER = {
    "login": "grigorieva",
    "password": "123456789"
}

CREATE_ORDER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

QUERY_COURIERID = 'orders?courierId=652294'
QUERY_NEARESTSTATION = 'orders?courierId=652294&nearestStation=["1", "2"]'
QUERY_LIMIT = 'orders?limit=10&page=0&nearestStation=["110"]'
QUERY_WRONG_COURIERID = 'orders?courierId=1'