
# Тестовое задание BRENDWALL

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)



## __Установка на локальном компьютере__
1. Клонируйте репозиторий:
    ```
    git clone git@github.com:Kirill67tyar/test-BRENDWALL.git
    ```
    или
    ```
     git clone https://github.com/Kirill67tyar/test-BRENDWALL.git
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
7. Собрать статику  (нужно для swagger):
    ```
    python manage.py collectstatic
    ```
8. Запустите проект:
    ```
    python manage.py runserver
    ```
7. Сайт будет доступен на странице:
    ```
    http://127.0.0.1:8000/api/
    ```
8. Документация будет доступна на странице:
    ```
    http://127.0.0.1:8000/swagger/
    ```
## __Пример запросов/ответов__

#### Получение списка категорий
####Request: [GET] http://127.0.0.1:8000/api/categories/ 
####Response samples:
```

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "name": "Еда",
            "slug": "eda",
            "image": "http://127.0.0.1:8000/media/categories/black-white-logo-fork-spoon_1166234-2104.jpg",
            "parent": null,
            "childrens": [
                {
                    "id": 5,
                    "name": "Печенье",
                    "slug": "pechene",
                    "image": "/media/categories/cookies-logo.jpg",
                    "parent": 2,
                    "childrens": null
                },
                {
                    "id": 6,
                    "name": "Пицца",
                    "slug": "pizza",
                    "image": "/media/categories/pizza-logo.jpg",
                    "parent": 2,
                    "childrens": null
                }
            ]
        },
        {
            "id": 1,
            "name": "Напитки",
            "slug": "napitki",
            "image": "http://127.0.0.1:8000/media/categories/1000_F_283327619_rnfUpLgzfn0PD1riXgiNMk2QSORJjbRR.jpg",
            "parent": null,
            "childrens": [
                {
                    "id": 3,
                    "name": "Кофе",
                    "slug": "kofe",
                    "image": "/media/categories/coffee-logo.jpg",
                    "parent": 1,
                    "childrens": null
                },
                {
                    "id": 4,
                    "name": "Чай",
                    "slug": "chaj",
                    "image": "/media/categories/tea-logo.jpg",
                    "parent": 1,
                    "childrens": null
                }
            ]
        }
    ]
}
```
#### Получение списка продуктов
####Request: [GET] http://127.0.0.1:8000/api/products/ 
####Response samples:
```
{
    "count": 18,
    "next": "http://127.0.0.1:8000/api/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Кофе1",
            "slug": "kofe1",
            "category": "Напитки",
            "subcategory": "Кофе",
            "price": "3.12",
            "image_small": "http://127.0.0.1:8000/media/CACHE/images/products/original/close-up-hand-pouring-milk-in-coffee-cup_23-2148865584/6f3887f82b54da4e4dad9720ad7283a8.jpg",
            "image_medium": "http://127.0.0.1:8000/media/CACHE/images/products/original/close-up-hand-pouring-milk-in-coffee-cup_23-2148865584/dda7862f8480b169862bdd333d663d53.jpg",
            "image_large": "http://127.0.0.1:8000/media/CACHE/images/products/original/close-up-hand-pouring-milk-in-coffee-cup_23-2148865584/d2d4c176e6f8b7b6023ac066b116d24b.jpg"
        },
        {
            "id": 2,
            "name": "Кофе2",
            "slug": "kofe2",
            "category": "Напитки",
            "subcategory": "Кофе",
            "price": "12345678.91",
            "image_small": "http://127.0.0.1:8000/media/CACHE/images/products/original/coffee-cup-wooden-table-dark-wall/c795436ed7295a72b4a7758032335b1d.jpg",
            "image_medium": "http://127.0.0.1:8000/media/CACHE/images/products/original/coffee-cup-wooden-table-dark-wall/521128280ccb105e478236ddfe205717.jpg",
            "image_large": "http://127.0.0.1:8000/media/CACHE/images/products/original/coffee-cup-wooden-table-dark-wall/76f2217af47f365869ef49c57b961d3c.jpg"
        },
        {
            "id": 3,
            "name": "Кофе3",
            "slug": "kofe3",
            "category": "Напитки",
            "subcategory": "Кофе",
            "price": "3211.00",
            "image_small": "http://127.0.0.1:8000/media/CACHE/images/products/original/coffee-machine-making-a-perfect-cup-of-coffee_23-2151699668/847e7e4e916f4b74dbb9a43041353f66.jpg",
            "image_medium": "http://127.0.0.1:8000/media/CACHE/images/products/original/coffee-machine-making-a-perfect-cup-of-coffee_23-2151699668/e741c88b5cee8be20330c72a50477c1e.jpg",
            "image_large": "http://127.0.0.1:8000/media/CACHE/images/products/original/coffee-machine-making-a-perfect-cup-of-coffee_23-2151699668/78b5ea64649092e189d3ace7d8a1f5dc.jpg"
        },
        {
            "id": 4,
            "name": "Кофе4",
            "slug": "kofe4",
            "category": "Напитки",
            "subcategory": "Кофе",
            "price": "32112.12",
            "image_small": "http://127.0.0.1:8000/media/CACHE/images/products/original/person-serving-a-cup-of-coffee_1286-227/89acb0d6800d4d7443ebd7c1b45efdb1.jpg",
            "image_medium": "http://127.0.0.1:8000/media/CACHE/images/products/original/person-serving-a-cup-of-coffee_1286-227/4d8e73857b04b4ebc2339bbe113c69f0.jpg",
            "image_large": "http://127.0.0.1:8000/media/CACHE/images/products/original/person-serving-a-cup-of-coffee_1286-227/de0cee6199b49f78fa1107399be6608b.jpg"
        },
        {
            "id": 5,
            "name": "Печенье1",
            "slug": "pechene1",
            "category": "Еда",
            "subcategory": "Печенье",
            "price": "312.32",
            "image_small": "http://127.0.0.1:8000/media/CACHE/images/products/original/close-up-chocolate-cookies_23-2148628343/5f742dac9e70af2c7ab6d2b30e598429.jpg",
            "image_medium": "http://127.0.0.1:8000/media/CACHE/images/products/original/close-up-chocolate-cookies_23-2148628343/5081fea9893beb20d3eed309b2fda0d5.jpg",
            "image_large": "http://127.0.0.1:8000/media/CACHE/images/products/original/close-up-chocolate-cookies_23-2148628343/4f9a0f08d1f99376eea300479dd701e7.jpg"
        },
        {
            "id": 6,
            "name": "Печенье2",
            "slug": "pechene2",
            "category": "Еда",
            "subcategory": "Печенье",
            "price": "909.12",
            "image_small": "http://127.0.0.1:8000/media/CACHE/images/products/original/close-up-cookies-with-nuts_23-2148837112/ca548c55cc1f665c33800ee4fda6fb2c.jpg",
            "image_medium": "http://127.0.0.1:8000/media/CACHE/images/products/original/close-up-cookies-with-nuts_23-2148837112/18e7b8fdc56ce01d2f2082ed134fa6b7.jpg",
            "image_large": "http://127.0.0.1:8000/media/CACHE/images/products/original/close-up-cookies-with-nuts_23-2148837112/bb8024cecb02d92927cf8b57cad6e817.jpg"
        },
        {
            "id": 7,
            "name": "Печенье3",
            "slug": "pechene3",
            "category": "Еда",
            "subcategory": "Печенье",
            "price": "9091.13",
            "image_small": "http://127.0.0.1:8000/media/CACHE/images/products/original/delicious-cookies-table_23-2148837156/3fb4b09d16bbe2becd34b646f3c54074.jpg",
            "image_medium": "http://127.0.0.1:8000/media/CACHE/images/products/original/delicious-cookies-table_23-2148837156/2e3b5f284bb2d0a9beb60ff0e0fcef49.jpg",
            "image_large": "http://127.0.0.1:8000/media/CACHE/images/products/original/delicious-cookies-table_23-2148837156/1ffe51f39faf1476f3577752c5c251f3.jpg"
        },
        {
            "id": 8,
            "name": "Печенье4",
            "slug": "pechene4",
            "category": "Еда",
            "subcategory": "Печенье",
            "price": "13313.13",
            "image_small": "http://127.0.0.1:8000/media/CACHE/images/products/original/paper-bag-with-delicious-cookies-table_23-2148837153/f8e19f4a59430d51aacd41e97f4ea571.jpg",
            "image_medium": "http://127.0.0.1:8000/media/CACHE/images/products/original/paper-bag-with-delicious-cookies-table_23-2148837153/5c4e5456259ae6432f0e51865a4f5f6f.jpg",
            "image_large": "http://127.0.0.1:8000/media/CACHE/images/products/original/paper-bag-with-delicious-cookies-table_23-2148837153/6eb730dd237f886cdce02504a3f11456.jpg"
        },
        {
            "id": 9,
            "name": "Печенье5",
            "slug": "pechene5",
            "category": "Еда",
            "subcategory": "Печенье",
            "price": "931.13",
            "image_small": "http://127.0.0.1:8000/media/CACHE/images/products/original/view-pepernoten-dessert-still-life_23-2149766671/b9c9e4024d8534cc81b804c902fe05c5.jpg",
            "image_medium": "http://127.0.0.1:8000/media/CACHE/images/products/original/view-pepernoten-dessert-still-life_23-2149766671/979bc779e1b9310f231c5582938d0c01.jpg",
            "image_large": "http://127.0.0.1:8000/media/CACHE/images/products/original/view-pepernoten-dessert-still-life_23-2149766671/78bbb43cc8e72ebd98ce570c5c96bca3.jpg"
        },
        {
            "id": 15,
            "name": "Пицца1",
            "slug": "picca1",
            "category": "Еда",
            "subcategory": "Пицца",
            "price": "3123.13",
            "image_small": "http://127.0.0.1:8000/media/CACHE/images/products/original/delicious-pizza-studio_23-2151846549/d244334f335f4fb67d20ee7cf4ff86cb.jpg",
            "image_medium": "http://127.0.0.1:8000/media/CACHE/images/products/original/delicious-pizza-studio_23-2151846549/2f143a517762bf2a3fadca8608ee8442.jpg",
            "image_large": "http://127.0.0.1:8000/media/CACHE/images/products/original/delicious-pizza-studio_23-2151846549/d3c15166295d04b0fd9671845ea73d65.jpg"
        }
    ]
}
```



###Добавление нового продукта: Request: [POST] http://127.0.0.1:8000/api/products/ 
###Response samples:
```
	{
		name: "new-pi",
		description: "описание new-pi",
		price: "3.14"
	}
```
### Основная страница доступна [GET]/[POST] http://127.0.0.1:8000/


### __Технологии__
* [Python 3.10.12](https://www.python.org/doc/)
* [Django 4.2.10](https://docs.djangoproject.com/en/4.2/)
* [Django REST Framework  3.14.0](https://www.django-rest-framework.org/)

### Авторство

 1. [BrendWall](https://brendwall.ru/).
 2. [Кирилл Богомолов](https://github.com/Kirill67tyar).