
from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
        'euro_shipping',
        'is_active',
        'available_quantity',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
