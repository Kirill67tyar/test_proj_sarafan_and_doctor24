from decimal import Decimal

import pytest
from django.test import Client
from django.urls import reverse

from products.models import Cart, CartItem, Category, Product


@pytest.fixture
def auth_client(django_user_model):
    """Фикстура создания автора комментария."""
    return django_user_model.objects.create(username='Кама Пуля')


@pytest.fixture
def owner_auth_client(auth_client):
    """Фикстура логина автора комментария."""
    client = Client()
    client.force_login(auth_client)
    return client


@pytest.fixture
def category():
    """Фикстура создания категории."""
    return Category.objects.create(
        name='Категория 1',
    )


@pytest.fixture
def subcategory(category):
    """Фикстура создания подкатегории."""
    return Category.objects.create(
        name='Подкатегория 1',
        parent=category,
    )


@pytest.fixture
def product(subcategory):
    """Фикстура создания продукта."""
    return Product.objects.create(
        name='Продукт 1',
        category=subcategory,
        price=Decimal('3.14'),
    )


@pytest.fixture
def cart(auth_client):
    """Фикстура создания корзины."""
    return Cart.objects.create(owner=auth_client)


@pytest.fixture
def cartitem(cart, product):
    """Фикстура логина автора комментария."""
    return CartItem.objects.create(
        cart=cart,
        product=product,
        quantity=3,
    )


@pytest.fixture
def cart_list_url():
    """Фикстура урла для списка товаров в корзине."""
    return reverse('api:cart-list')


@pytest.fixture
def detail_url(product):
    """Фикстура урла для списка товаров в корзине."""
    return reverse(
        'api:cart-detail',
        kwargs={
            'pk': product.pk,
        }
    )


@pytest.fixture
def cartitem_data(product):
    """Фикстура данных для добавления товара в корзину."""
    return {
        'product': product.pk,
        'quantity': 3
    }


@pytest.fixture
def cartitem_update_data(product):
    """Фикстура данных для изменения количества товара в корзине."""
    return {
        'product': product.pk,
        'quantity': 5
    }
