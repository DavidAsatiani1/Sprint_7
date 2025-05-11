class Endpoint:
    SCOOTER_URL = 'http://qa-scooter.praktikum-services.ru'
    # POST
    CREATE_COURIER = f'{SCOOTER_URL}/api/v1/courier'
    LOGIN_COURIER = f'{SCOOTER_URL}/api/v1/courier/login'
    CREATE_ORDER = f'{SCOOTER_URL}/api/v1/orders'
    # GET
    ORDER_LIST = f'{SCOOTER_URL}/api/v1/orders'
    GET_ORDER_TRACK = f'{SCOOTER_URL}/api/v1/orders/track'



class Message:
    CREATE_COURIER = '{"ok":true}'
    CREATE_EXISTING_COURIER = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    CREATE_COURIER_WITHOUT_LOGIN = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    LOGING_COURIER = 'id'
    LOGING_COURIER_WITHOUT_DATA = '{"code":400,"message":"Недостаточно данных для входа"}'
    LOGING_NOT_EXISTING_COURIER = '{"code":404,"message":"Учетная запись не найдена"}'
    CREATE_ORDER = 'track'
    LIST_ORDERS = 'orders'


class User:
    user = {
        'firstname': 'Иван',
        'lastname': 'Иванов',
        'address': 'Москва',
        'metroStation': 5,
        'phone': '+79876543210',
        'rentTime': 2,
        'deliveryDate': '09-05-2025',
        'comment': '',
        'color': []
    }