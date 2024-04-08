from create_data import *


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа для авторизованного пользователя')
    @allure.description('Используется метод создания нового пользователя и метод получения списка ингредиентов. В '
                        'запрос создания заказа передается токен пользователя и список ингредиентов. Выполняется '
                        'проверка статуса ответа и значения показателя success')
    def test_create_order_with_auth_and_ingredients(self):
        user_info = register_new_user_and_return_user_info()
        ingredient_list = get_ingredients()
        payload = {"ingredients": ingredient_list}
        response = requests.post(f'{Data.burger_main}{Data.endpoint_order}', headers={'Authorization': user_info.get("token")}, data=payload)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Проверка успешного создания заказа для неавторизованного пользователя')
    @allure.description('Используется метод получения списка ингредиентов. В запрос создания заказа передается список '
                        'ингредиентов без передачи токена пользователя. Выполняется проверка статуса ответа и '
                        'значения показателя success')
    def test_create_order_ingredients_and_without_auth(self):
        ingredient_list = get_ingredients()
        payload = {"ingredients": ingredient_list}
        response = requests.post(f'{Data.burger_main}{Data.endpoint_order}', data=payload)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Проверка ошибки создания заказа для авторизованного пользователя с пустым списком ингредиентов')
    @allure.description('Используется метод создания нового пользователя. В запрос создания заказа передается токен '
                        'пользователя, при этом список ингредиентов пуст. Выполняется проверка статуса ответа, '
                        'значения показателя success и текст ошибки')
    def test_create_order_with_auth_and_without_ingredients(self):
        user_info = register_new_user_and_return_user_info()
        payload = {"ingredients": ""}
        response = requests.post(f'{Data.burger_main}{Data.endpoint_order}', headers={'Authorization': user_info.get("token")}, data=payload)
        assert response.status_code == 400 and response.json()["success"] == False and response.json()['message'] == Data.answer_order_without_ingredients

    @allure.title('Проверка ошибки создания заказа для неавторизованного пользователя с пустым списком ингредиентов')
    @allure.description('В запрос создания заказа не передается токен авторизации пользователя, при этом список '
                        'ингредиентов пуст. Выполняется проверка статуса ответа, значения показателя success и текст '
                        'ошибки')
    def test_create_order_without_auth_and_without_ingredients(self):
        payload = {"ingredients": ""}
        response = requests.post(f'{Data.burger_main}{Data.endpoint_order}', data=payload)
        assert response.status_code == 400 and response.json()["success"] == False and response.json()['message'] == Data.answer_order_without_ingredients

    @allure.title('Проверка ошибки создания заказа при наличии некорректного значения в списке ингредиентов')
    @allure.description('Используется метод создания нового пользователя. В запрос создания заказа передается токен '
                        'пользователя, при этом список ингредиентов содержит некорректный id. Выполняется проверка '
                        'статуса ответа, значения показателя success и текст ошибки')
    def test_create_order_with_incorrect_ingredients(self):
        user_info = register_new_user_and_return_user_info()
        payload = {"ingredients": "11111"}
        response = requests.post(f'{Data.burger_main}{Data.endpoint_order}', headers={'Authorization': user_info.get("token")}, data=payload)
        assert response.status_code == 500 and Data.answer_error_server in response.text
