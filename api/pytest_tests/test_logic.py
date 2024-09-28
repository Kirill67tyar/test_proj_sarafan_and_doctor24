import json
from http import HTTPStatus

import pytest
from django.urls import reverse

from products.models import CartItem


@pytest.mark.django_db
def test_anonymous_user_cant_add_product_to_cart(client,
                                                 cart_list_url,
                                                 cartitem_data):
    """
    Тест на то, что незалогиненный пользователь не может
    добавить товар в корзину.
    """
    response = client.post(
        cart_list_url,
        data=json.dumps(cartitem_data),
        content_type='application/json'
    )
    cartitem_count = CartItem.objects.count()
    assert cartitem_count == 0
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_user_can_add_product_to_cart(owner_auth_client,
                                      product,
                                      auth_client,
                                      cart_list_url,
                                      cartitem_data,):
    """
    Тест на то, что залогиненный пользователь может
    добавить товар в корзину.
    """
    response = owner_auth_client.post(
        cart_list_url,
        data=json.dumps(cartitem_data),
        content_type='application/json'
    )
    cartitem_count = CartItem.objects.count()
    cart_item = CartItem.objects.get()
    assert cartitem_count == 1
    assert cart_item.quantity == cartitem_data['quantity']
    assert cart_item.cart.owner == auth_client
    assert cart_item.product == product
    assert response.status_code == HTTPStatus.CREATED


def test_owner_can_delete_product_from_cart(owner_auth_client,
                                            cartitem,
                                            detail_url):
    """Тест на то, что владелец корзины может удалить товар из неё."""
    response = owner_auth_client.delete(detail_url)
    cartitem_count = CartItem.objects.count()
    assert cartitem_count == 0
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_owner_can_edit_quabtity(owner_auth_client,
                                 cartitem,
                                 detail_url,
                                 cartitem_update_data):
    """
    Тест на то, что владелец корзины может изменить
     количества товара.
    """
    response = owner_auth_client.put(
        detail_url,
        data=json.dumps(cartitem_update_data),
        content_type='application/json'
    )
    cartitem.refresh_from_db()
    assert cartitem.quantity == cartitem_update_data['quantity']
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    argnames=('view_name',),
    argvalues=(
        ('api:categories-list',),
        ('api:products-list',),
    ),
)
@pytest.mark.django_db
def test_page_availability(client, view_name):
    """
    Тест на доступность страниц:
     список категорий и список продуктов для всех пользователей.
    """
    response = client.get(reverse(view_name))
    assert response.status_code == HTTPStatus.OK
