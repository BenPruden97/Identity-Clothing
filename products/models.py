from django.db import models
from decimal import Decimal

from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
      
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    SIZE_CHOICES = (
        ('XXSmall','XXS'),
        ('XSmall','XS'),
        ('Small','S'),
        ('Medium','M'),
        ('Large','L'),
        ('XLarge','XL'),
        ('XXLarge','XXL'),
    )

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_on_sale = models.BooleanField(default=False)
    sale_percentage = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_size = models.CharField(max_length=7, choices=SIZE_CHOICES)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def calculate_sale_price(self):
        """
        Calculate the price of the clothing item using the sale_percentage value
        Credit: https://helperbyte.com/questions/77886/django-how-to-make-a-discount-for-the-item
        """
        product_sale = Decimal(self.price * (
            100 - self.sale_percentage) / 100).quantize(Decimal('0.00'))
        return product_sale


PRODUCT_RATING = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class ProductReview(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_add_text = models.TextField(max_length=254)
    review_add_rating = models.IntegerField(choices=PRODUCT_RATING)
    date_created = models.DateField(auto_now_add=True)
