from django.shortcuts import render

from products.models import Product
from django.db.models import Q

# Create your views here.

def index(request):
    """
    View to return the index.html page
    """

    best_seller_products = Product.objects.filter(Q(name="Men's Adidas Overhead Hoodie") |
                                                  Q(name="Men's Star Wars Overhead Hoodie") |
                                                  Q(name="Men's Black Nike T-Shirt") |
                                                  Q(name="Women's White New York T-Shirt") |
                                                  Q(name="Women's Adidas Overhead Hoodie") |
                                                  Q(name="Women's Black Nike Shorts") |
                                                  Q(name="Men's Black Nike Overhead Hoodie") |
                                                  Q(name="Men's Blue Nike T-Shirt") |
                                                  Q(name="Women's White Vogue T-Shirt"))

    context = {
        'best_seller_products': best_seller_products,
    }

    return render(request, 'index.html', context)
