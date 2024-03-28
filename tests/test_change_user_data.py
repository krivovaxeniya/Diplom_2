from create_data import *


class TestChangeUserData:

    @allure.title('Проверка успешного изменения пароля авторизованного пользователя')
    @allure.description('Используется метод создания нового пользователя. В запрос на изменение данных пользователя '
                        'отправляется токен пользователя и обновленный пароль. Выполняется проверка статуса ответа, '
                        'значения показателя success и соответствие возвращаемого в ответе email указанному в запросе '
                        'на изменение')
    def test_change_authorizated_user_password(self):
        user_info = register_new_user_and_return_user_info()
        payload = {"email": user_info.get("email"),
                   "password": "password",
                   "name": user_info.get("name")}
        response = requests.patch(f'{Urls.burger_main}/api/auth/user',  headers={'Authorization': user_info.get("token")}, data=payload)
        assert response.status_code == 200 and response.json()["success"] == True and response.json()['user']['email'] == payload.get('email')

    @allure.title('Проверка успешного изменения email авторизованного пользователя')
    @allure.description('Используется метод создания нового пользователя. В запрос на изменение данных пользователя '
                        'отправляется токен пользователя и обновленный email. Выполняется проверка статуса ответа, '
                        'значения показателя success и соответствие возвращаемого в ответе email указанному в запросе '
                        'на изменение')
    def test_change_authorizated_user_email(self):
        user_info = register_new_user_and_return_user_info()
        payload = {"email": f'test_change_mail{random.randint(0, 1000)}.ya.ru',
                   "password": user_info.get("password"),
                   "name": user_info.get("name")}
        response = requests.patch(f'{Urls.burger_main}/api/auth/user',  headers={'Authorization': user_info.get("token")},data=payload)
        assert response.status_code == 200 and response.json()["success"] == True and response.json()['user']['email'] == payload.get('email')

    @allure.title('Проверка успешного изменения имени авторизованного пользователя')
    @allure.description('Используется метод создания нового пользователя. В запрос на изменение данных пользователя '
                        'отправляется токен пользователя и обновленное имя. Выполняется проверка статуса ответа, '
                        'значения показателя success и соответствие возвращаемого в ответе имени указанному в запросе '
                        'на изменение')
    def test_change_authorizated_user_name(self):
        user_info = register_new_user_and_return_user_info()
        payload = {"email": user_info.get("email"),
                   "password": user_info.get("password"),
                   "name": "Ostap"}
        response = requests.patch(f'{Urls.burger_main}/api/auth/user',  headers={'Authorization': user_info.get("token")},data=payload)
        assert response.status_code == 200 and response.json()["success"] == True and response.json()['user']['name'] == payload.get('name')

    @allure.title('Проверка ошибки изменения имени для авторизованного пользователя')
    @allure.description('Используется метод создания нового пользователя. В запрос на изменение данных пользователя '
                        'отправляется измененное имя, при этом не выполняется отправка токена авторизации. '
                        'Выполняется проверка статуса ответа, значения показателя success и текста ошибки')
    def test_change_not_authorizated_user_data(self):
        user_info = register_new_user_and_return_user_info()
        payload = {"email": user_info.get("email"),
                   "password": user_info.get("password"),
                   "name": "Ostap"}
        response = requests.patch(f'{Urls.burger_main}/api/auth/user', data=payload)
        assert response.status_code == 401 and response.json()["success"] == False and response.json()['message'] == 'You should be authorised'
