import pytest
from create_data import *


class TestLoginUser:

    @allure.title('Проверка успешной авторизации зарегистрированного пользователя')
    @allure.description('Используется метод создания нового пользователя. Данные созданного пользователя '
                        'используются в запросе на авторизацию. Выполняется проверка статуса ответа, '
                        'значения показателя success и соответствие возвращаемого в ответе email указанному при '
                        'авторизации')
    def test_login_created_user(self):
        user_data = register_new_user_and_return_user_info()
        payload = {"email": user_data.get('email'),
                   "password": user_data.get('password')}
        response = requests.post(f'{Urls.burger_main}/api/auth/login', data=payload)
        assert response.status_code == 200 and response.json()["success"] == True and response.json()['user']['email'] == payload.get('email')

    @allure.title('Проверка ошибки авторизации при вводе некорректного email или пароля')
    @allure.description('Используется метод создания нового пользователя. В запросе на авторизацию используются '
                        'email/пароль, отличный от данных регистрации. Выполняется проверка статуса ответа, '
                        'значения показателя success и текста ошибки')
    @pytest.mark.parametrize('email, password',
                             [[register_new_user_and_return_user_info().get("email"), f'{register_new_user_and_return_user_info().get("password")}1'],
                              [f'{register_new_user_and_return_user_info().get("email")}1', register_new_user_and_return_user_info().get("password")]
                              ])
    def test_login_with_incorrect_data(self, email, password):
        payload = {"email": email,
                   "password": password}
        response = requests.post(f'{Urls.burger_main}/api/auth/login', data=payload)
        assert response.status_code == 401 and response.json()["success"] == False and response.json()['message'] == 'email or password are incorrect'
