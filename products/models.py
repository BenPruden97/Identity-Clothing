from django.db import models


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
    rating = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    product_size = models.CharField(max_length=7, choices=SIZE_CHOICES)
    product_sale = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
