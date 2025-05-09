import allure
import requests
from data import Endpoint, Message


@allure.title('Тест: Получить список заказов')
class TestListOrder:
    @allure.step('Отправить GET-запрос для получения списка заказов')
    def test_list_order(self):
        with allure.step('Отправить GET-запрос для получения списка заказов'):
            r = requests.get(Endpoint.ORDER_LIST)

        with allure.step('Проверить статус-код ответа'):
            assert r.status_code == 200

        with allure.step('Проверить наличие сообщения в ответе'):
            assert Message.LIST_ORDERS in r.text

