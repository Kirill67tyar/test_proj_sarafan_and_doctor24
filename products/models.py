from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from mptt.models import MPTTModel, TreeForeignKey
from slugify import slugify

from main import constants


User = get_user_model()


class Category(MPTTModel):
    name = models.CharField(
        max_length=100,
        verbose_name='Категория',
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        verbose_name='url категории',
    )
    image = models.ImageField(
        upload_to='categories/',
        verbose_name='Изображение',
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='childrens',
        verbose_name='Родительская категория',
    )

    class MPTTMeta:
        # новые подкатегории будут вставляться по алфавиту
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def clean(self):
        if self.parent and self.parent.level >= constants.MAX_DEPTH:
            raise ValidationError(
                constants.MAX_DEPTH_MESSAGE_ERROR
            )
        if self == self.parent:
            raise ValidationError(
                constants.SAME_CATEGORY_AND_SUBCATEGORY_MESSAGE_ERROR
            )
        if self.pk:
            if self.childrens.exists() and self.parent:
                raise ValidationError(
                    constants.CATEGORY_CANNOT_BE_SUBCATEGORY_MESSAGE_ERROR
                )
        super().clean()

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Продукт',
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
        verbose_name='url продукта',
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
    )
    # оригинальное изображение
    image = models.ImageField(
        upload_to='products/original/',
        verbose_name='Изображение',
    )

    #  image_small, image_medium, image_large -
    # генерация разных размеров изображений "на лету"
    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 90},
    )

    image_medium = ImageSpecField(
        source='image',
        processors=[ResizeToFill(500, 500)],
        format='JPEG',
        options={'quality': 90},
    )

    image_large = ImageSpecField(
        source='image',
        processors=[ResizeToFill(800, 800)],
        format='JPEG',
        options={'quality': 90},
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

    def clean(self):
        if not self.category.parent:
            raise ValidationError(
                constants.SELECT_SUBCATEGORY_MESSAGE_ERROR
            )
        super().clean()

    def save(self, *args, **kwargs):
        if not self.category.parent:
            raise ValidationError(
                constants.SELECT_SUBCATEGORY_MESSAGE_ERROR
            )
        self.name = self.name.title()
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Cart(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Покупатель',
    )
    products = models.ManyToManyField(
        Product,
        through='CartItem',
        verbose_name='Продукты',
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('pk',)
        default_related_name = 'carts'

    def __str__(self):
        return f'Корзина - {self.pk}'


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        default=1
    )

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзинах'
        ordering = ('pk',)
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'product', ],
                name='unique_key_cart_product'
            ),
        ]

    def __str__(self):
        return f'Товар в корзине ({self.pk})'
