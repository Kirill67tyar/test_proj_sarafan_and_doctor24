
# Тестовое задание для Доктор24 и Сарафан

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

В данном проекте реализованы два задания:

1. **Проект магазина**:
   Реализован проект на Django с основным функционалом для магазина, включающим добавление товаров в корзину, а также работу с категориями и товарами.

2. **Генератор числовой последовательности**:
   Написана программа, которая выводит `n` первых элементов последовательности вида 122333444455555… (каждое число повторяется столько раз, чему оно равно).

## __Установка на локальном компьютере__
1. Клонируйте репозиторий:
    ```
    git clone https://github.com/Kirill67tyar/test_proj_sarafan_and_doctor24.git
    ```
    или
    ```
     git clone git@github.com:Kirill67tyar/test_proj_sarafan_and_doctor24.git
    ```
2. Установите и активируйте виртуальное окружение:
    ```
    python3 -m venv venv
    source venv/Scripts/activate  - для Windows
    source venv/bin/activate - для Linux
    ```
3. Установите зависимости:
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. Выполните миграции:
    ```
    python manage.py migrate
    ```
5. Загрузите фикстуры:
    ```
    python manage.py loaddata fixtures/test_db.json
    ```
6. Создайте суперпользователя:
    ```
    python manage.py createsuperuser
    ```
7. Соберите статику  (нужно для swagger):
    ```
    python manage.py collectstatic
    ```
8. Запустите тесты:
    ```
    pytest
    ```
9. Запустите проект:
    ```
    python manage.py runserver
    ```
10. API будет доступен на странице:
    ```
    http://127.0.0.1:8000/api/
    ```
11. Документация будет доступна на странице:
    ```
    http://127.0.0.1:8000/swagger/
    ```

### __Программа «Генератор числовой последовательности»__
1. Остановите локальный сервер комбинацией клавишь Ctrl+C:
2. Находясь в корневой директории запустите программу:
    ```
    python3 sequence_generator.py
    ```
3. Остановка программы - комбинация клавишь Ctrl+C или введите "exit":

### __Технологии__
* [Python 3.10.12](https://www.python.org/doc/)
* [Django 4.2.10](https://docs.djangoproject.com/en/4.2/)
* [Django REST Framework  3.14.0](https://www.django-rest-framework.org/)

### Авторство

[Кирилл Богомолов](https://github.com/Kirill67tyar).