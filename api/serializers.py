from rest_framework import serializers

from main import constants
from products.models import CartItem, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    childrens = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'image',
            'parent',
            'childrens',
        )

    def get_childrens(self, obj):
        if obj.level >= constants.MAX_DEPTH:
            return None
        serializer = CategorySerializer(obj.childrens.all(), many=True)
        return serializer.data


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(
        source='category.parent', read_only=True)
    subcategory = serializers.StringRelatedField(
        source='category', read_only=True)
    image_small = serializers.ImageField(read_only=True)
    image_medium = serializers.ImageField(read_only=True)
    image_large = serializers.ImageField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'category',
            'subcategory',
            'price',
            'image_small',
            'image_medium',
            'image_large',
        )


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=False)

    class Meta:
        model = CartItem
        fields = (
            'id',
            'product',
            'quantity',
        )


class CreateDeleteCartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())

    class Meta:
        model = CartItem
        fields = (
            'product',
            'quantity',
        )

    def validate(self, data):
        cart = self.context['cart']
        product = data['product']
        if CartItem.objects.filter(cart=cart, product=product).exists():
            raise serializers.ValidationError(
                constants.PRODUCT_ALREADY_IN_CART_MESSAGE_ERROR
            )
        return data

    def to_representation(self, value):
        serializer = CartItemSerializer(value)
        serializer.context['request'] = self.context['request']
        return serializer.data


class UpdateCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = (
            'quantity',
        )

    def to_representation(self, value):
        serializer = CartItemSerializer(value)
        serializer.context['request'] = self.context['request']
        return serializer.data
