from create_data import *


class TestGetOrderList:

    @allure.title('Проверка успешного получения списка заказов для авторизованного пользователя')
    @allure.description('Используется метод, создающий пользователя и заказ для пользователя. Токен пользователя, '
                        'имеющего заказ, передается в запрос для получения списка заказов. Выполняется проверка '
                        'статуса ответа, значения показателя success и список всех ключей в теле ответа')
    def test_get_order_list_for_auth_user(self):
        token = create_user_and_create_order()
        response = requests.get(f'{Urls.burger_main}/api/orders', headers={'Authorization': token})
        order_keys = ['_id', 'ingredients', 'status', 'name', 'createdAt', 'updatedAt', 'number']
        assert response.status_code == 200 and response.json()["success"] == True and list(response.json()["orders"][0].keys()) == order_keys

    @allure.title('Проверка ошибки получения списка заказов для неавторизованного пользователя')
    @allure.description('Отправляется запрос на получение списка заказов без передачи токена пользователя. '
                        'Выполняется проверка статуса ответа, значения показателя success и текст ошибки')
    def test_get_order_list_for_not_auth_user(self):
        response = requests.get(f'{Urls.burger_main}/api/orders')
        assert response.status_code == 401 and response.json()["success"] == False and response.json()['message'] == 'You should be authorised'