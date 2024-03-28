import pytest
from create_data import *


class TestCreateUser:

    @allure.title('Проверка успешного создания нового уникального пользователя')
    @allure.description('Отправляется запрос на создание нового пользователя с заполненными обязательными '
                        'параметрами. Выполняется проверка статуса ответа, значения показателя success и соответствие '
                        'возвращаемого в ответе email указанному при регистрации')
    def test_create_new_user(self):
        payload = {"email": f'slowpoke{random.randint(0, 1000)}@ya.ru',
                   "password": "12345678",
                   "name": "Ivan"
                   }
        response = requests.post(f'{Urls.burger_main}/api/auth/register', data=payload)
        assert response.status_code == 200 and response.json()["success"] == True and response.json()['user']['email'] == payload.get('email')

    @allure.title('Проверка возврата ошибки при создании пользователя, который уже зарегистрирован')
    @allure.description('Используется метод создания нового пользователя. Данные пользователя используются повторно '
                        'в запросе на регистрацию. Выполняется проверка статуса ответа, значения показателя success и'
                        ' текста ошибки')
    def test_create_existed_user(self):
        user_data = register_new_user_and_return_user_info()
        payload = {"email": user_data.get('email'),
                   "password": user_data.get('password'),
                   "name": user_data.get('name')}
        response = requests.post(f'{Urls.burger_main}/api/auth/register', data=payload)
        assert response.status_code == 403 and response.json()["success"] == False and response.json()['message'] == 'User already exists'

    @allure.title('Проверка возврата ошибки при создании пользователя в случае, когда не заполнен один обязательный показатель')
    @allure.description('Отправляются запросы на создание пользователя, в каждом из которых не заполнен один из '
                        'обязательный параметров - email, пароль или имя. Выполняется проверка статуса ответа, '
                        'значения показателя success и текста ошибки')
    @pytest.mark.parametrize('email, password, name',
                             [['test111@ya.ru', '1234567', ''],
                              ['test111@ya.ru', '', 'Ivan'],
                              ['', '12345678', 'Ivan']])
    def test_create_user_without_one_required_field(self, email, password, name):
        payload = {"email": email,
                   "password": password,
                   "name": name}
        response = requests.post(f'{Urls.burger_main}/api/auth/register', data=payload)
        assert response.status_code == 403 and response.json()["success"] == False and response.json()['message'] == 'Email, password and name are required fields'

