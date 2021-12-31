from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cashe_checkout_data/', views.cashe_checkout_data, name='cashe_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
