# Diplom_2
<h3>Автотесты, реализованные для сервиса Stellar Burgers</h3>

<h4>test_create_user.TestCreateUser - тесты для проверки создания пользователя</h4>
Проверка эндпоинта /api/auth/register</br>
Метод запроса <b>POST</b>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_create_new_user</td>
      <td>Проверка успешного создания нового уникального пользователя</td>
    </tr>
    <tr>
      <td>test_create_existed_user</td>
      <td>Проверка возврата ошибки при создании пользователя, который уже зарегистрирован</td>
    </tr>
    <tr>
      <td>test_create_user_without_one_required_field</td>
      <td>Проверка возврата ошибки при создании пользователя в случае, когда не заполнен один обязательный показатель</td>
    </tr>
  </tbody>
</table>

<h4>test_login_user.TestLoginUser - тесты для проверки авторизации пользователя</h4>
Проверка эндпоинта /api/auth/login</br>
Метод запроса <b>POST</b>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_login_created_user</td>
      <td>Проверка успешной авторизации зарегистрированного пользователя</td>
    </tr>
    <tr>
      <td>test_login_with_incorrect_data</td>
      <td>Проверка ошибки авторизации при вводе некорректного email или пароля</td>
    </tr>
  </tbody>
</table>

<h4>test_change_user_data.TestChangeUserData - тесты для проверки изменения данных пользователя</h4>
Проверка эндпоинта /api/auth/user</br>
Метод запроса <b>PATCH</b>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_change_authorizated_user_password</td>
      <td>Проверка успешного изменения пароля авторизованного пользователя</td>
    </tr>
    <tr>
      <td>test_change_authorizated_user_email</td>
      <td>Проверка успешного изменения email авторизованного пользователя</td>
    </tr>
    <tr>
      <td>test_change_authorizated_user_name</td>
      <td>Проверка успешного изменения имени авторизованного пользователя</td>
    </tr>
    <tr>
      <td>test_change_not_authorizated_user_data</td>
      <td>Проверка ошибки изменения имени для авторизованного пользователя</td>
    </tr>
  </tbody>
</table>

<h4>test_create_order.TestCreateOrder - тесты для проверки создания заказа</h4>
Проверка эндпоинта /api/orders</br>
Метод запроса <b>POST</b>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_create_order_with_auth_and_ingredients</td>
      <td>Проверка успешного создания заказа для авторизованного пользователя</td>
    </tr>
    <tr>
      <td>test_create_order_ingredients_and_without_auth</td>
      <td>Проверка успешного создания заказа для неавторизованного пользователя'</td>
    </tr>
    <tr>
      <td>test_create_order_with_auth_and_without_ingredients</td>
      <td>Проверка ошибки создания заказа для авторизованного пользователя с пустым списком ингредиентов</td>
    </tr>
    <tr>
      <td>test_create_order_without_auth_and_without_ingredients</td>
      <td>Проверка ошибки создания заказа для неавторизованного пользователя с пустым списком ингредиентов</td>
    </tr>
    <tr>
      <td>test_create_order_with_incorrect_ingredients</td>
      <td>Проверка ошибки создания заказа при наличии некорректного значения в списке ингредиентов</td>
    </tr>
  </tbody>
</table>

<h4>test_get_order_list.TestGetOrderList - тесты для проверки получения списка заказов пользователя</h4>
Проверка эндпоинта /api/orders</br>
Метод запроса <b>GET</b>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_get_order_list_for_auth_user</td>
      <td>Проверка успешного получения списка заказов для авторизованного пользователя</td>
    </tr>
    <tr>
      <td>test_get_order_list_for_not_auth_user</td>
      <td>Проверка ошибки получения списка заказов для неавторизованного пользователя</td>
    </tr>
  </tbody>
</table>

Для работы необходимы библиотеки: </br>
<li>pytest</li>
<li>requests</li>
<li>random</li>
<li>allure</li>

Запуск тестов:  <b>pytest -v</b> </br>
Построение отчета о тестировании: <b>allure serve allure_results</b> 