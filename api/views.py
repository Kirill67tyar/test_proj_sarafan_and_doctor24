from django.contrib.auth import get_user_model
from django.db import DatabaseError
from django.db.models import F, Sum
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.permissions import IsAuthenticatedAndOwner
from api.serializers import (CartItemSerializer, CategorySerializer,
                             CreateDeleteCartItemSerializer, ProductSerializer,
                             UpdateCartItemSerializer)
from api.viewsets import ReadOnlyListModelViewSet
from main import constants
from products.models import Cart, CartItem, Category, Product


User = get_user_model()


class CategoryModelViewSet(ReadOnlyListModelViewSet):
    serializer_class = CategorySerializer
    queryset = (Category.objects
                .filter(parent=None)
                .prefetch_related('childrens'))


class ProductModelViewSet(ReadOnlyListModelViewSet):
    serializer_class = ProductSerializer
    queryset = (Product.objects
                .select_related('category')
                .prefetch_related('category__parent'))


class CartModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedAndOwner,)
    serializer_class = CartItemSerializer
    pagination_class = None
    queryset = CartItem.objects.all()
    http_method_names = [
        'get',
        'post',
        'put',
        'delete',
        'options',
    ]
    token_param = openapi.Parameter(
        'Authorization',  # Имя заголовка
        openapi.IN_HEADER,  # Положение заголовка (header)
        description='Токен для авторизации. Формат: Token <token>',
        type=openapi.TYPE_STRING,  # Тип данных
        required=True,  # Обязательность заголовка
    )

    def get_serializer_class(self):
        if self.action in ['create', 'destroy',]:
            return CreateDeleteCartItemSerializer
        if self.action in ['update',]:
            return UpdateCartItemSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            # проверка для swagger, иначе ошибка
            # несмотря на то, что задан permission:
            # permission_classes = (IsAuthenticatedAndOwner,)
            return CartItem.objects.none()
        try:
            cart = self.request.user.cart
            queryset = cart.cartitem_set.all()
        except User.cart.RelatedObjectDoesNotExist:
            queryset = CartItem.objects.none()
        return queryset.select_related('product').annotate(
            price_by_product=F('quantity') * F('product__price'),
        )

    @swagger_auto_schema(manual_parameters=[token_param])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[token_param])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[token_param])
    def create(self, request, *args, **kwargs):
        """
        Переопределил метод create чтобы получать/создавать корзину
        для пользователя, а также передавать её в контекст сериалайзера.
        """
        try:
            cart, _ = Cart.objects.get_or_create(owner=request.user)
        except DatabaseError:
            raise APIException(
                constants.CREATION_CART_MESSAGE_ERROR,
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        serializer = self.get_serializer(
            data=request.data,
            context={
                'cart': cart,
                'request': request,
            }
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, cart)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer, cart):
        serializer.save(cart=cart)

    @swagger_auto_schema(manual_parameters=[token_param])
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        aggregated_data = queryset.aggregate(
            total_quantity=Sum('quantity'),
            total_price=Sum('price_by_product'),
        )
        return Response(
            data={
                'total_quantity': aggregated_data['total_quantity'] or 0,
                'total_price': aggregated_data['total_price'] or 0,
                'items': serializer.data,
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(manual_parameters=[token_param])
    @action(
        detail=False,
        methods=['delete'],
        url_path='clear',
        url_name='clear-cart'
    )
    def clear_cart(self, request):
        try:
            cart = self.request.user.cart
        except User.cart.RelatedObjectDoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
            )

        cart.cartitem_set.all().delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )
