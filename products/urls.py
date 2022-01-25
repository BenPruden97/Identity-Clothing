from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('products_on_sale/', views.products_on_sale, name='products_on_sale'),
    path('search/', views.search, name='search'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_product_review/<int:product_id>/', views.add_product_review, name='add_product_review'),
    path('edit_product_review/<int:productreview_id>/', views.edit_product_review, name='edit_product_review'),
    path('delete_product_review/<int:productreview_id>/', views.delete_product_review, name='delete_product_review'),
]
