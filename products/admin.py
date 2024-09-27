from django.contrib import admin

from products.models import Cart, Category, Product


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',],}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name',],}


admin.site.register(Category, CategoryAdmin,)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
