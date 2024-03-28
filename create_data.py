import allure
import requests
import random
import string
from urls import Urls


@allure.step('Используется метод регистрации нового пользователя, который возвращает список из email, пароля и имени')
def register_new_user_and_return_user_info():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    user_info = {}
    email = f'{generate_random_string(10)}@ya.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": name}
    response = requests.post(f'{Urls.burger_main}/api/auth/register', data=payload)
    if response.status_code == 200:
        user_info = {"email": email,
                     "password": password,
                     "name": name,
                     "token": response.json()["accessToken"]}
    return user_info


@allure.step('Используется метод получения списка ингредиентов, откуда произвольно выбираются два элемента и '
             'добавляются в список')
def get_ingredients():
    response = requests.get(f'{Urls.burger_main}/api/ingredients')
    ingredients = response.json()['data']
    random_ingr_id_1 = random.choice(list(ingredients))['_id']
    random_ingr_id_2 = random.choice(list(ingredients))['_id']
    random_ingr_list = [random_ingr_id_1, random_ingr_id_2]
    return random_ingr_list


@allure.step('Используются методы создания нового пользователя и получения списка ингредиентов, для нового '
             'пользователя создается заказ с выбранными ингредиентами')
def create_user_and_create_order():
    user_data = register_new_user_and_return_user_info()
    ingredient_list = get_ingredients()
    payload = {"ingredients": ingredient_list}
    response = requests.post(f'{Urls.burger_main}/api/orders', headers={'Authorization': user_data.get("token")}, data=payload)
    return user_data.get("token")
