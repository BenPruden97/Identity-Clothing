from django.contrib import admin
from .models import Product, Category, ProductSize

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'category',
        'price',
        'product_rating',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = (
        'product_size',
        'product_size_name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
