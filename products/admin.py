"""
This is the product admin to create admin
views for Products, Categories and Product Reviews
"""

from django.contrib import admin
from .models import Product, Category, ProductReview

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """
    Create Admin views for products
    """
    list_display = (
        'name',
        'description',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Create Admin views for Catgories
    """
    list_display = (
        'friendly_name',
        'name'
    )


class ProductReviewAdmin(admin.ModelAdmin):
    """
    Create Admin views for Product Reviews
    """
    list_display = (
        'user',
        'product',
        'review_add_text',
        'review_add_rating',
        'date_created',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
