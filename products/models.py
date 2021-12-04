from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name


class ProductSize(models.Model):
    product_size = models.CharField(max_length=254)
    product_size_name = models.CharField(max_length=254, default='Small')

    def __str__(self):
        return str(self.product_size)

    def get_product_size_name(self):
        return self.product_size_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_id = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_rating = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    product_sale = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_option = models.ManyToManyField('ProductSize', blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
