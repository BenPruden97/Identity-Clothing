"""
signals.py file was created the calculate the average rating
for each product once created, updated deleted
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ProductReview


@receiver(post_save, sender=ProductReview)
def ben_find_averages(sender, instance, created, **kwargs):
    """
    Used to Calculate the average rating of a product
    once a product review has been created or updated
    """

    calculate_average_rating(instance)


@receiver(post_delete, sender=ProductReview)
def ben_averages(sender, instance, **kwargs):
    """
    Update product average_rating on product review delete
    """
    calculate_average_rating(instance)


def calculate_average_rating(instance):
    """ Calculate product average rating """

    current_product = instance.product

    current_product_reviews = ProductReview.objects.filter(
                              product=current_product)
    product_sum = 0
    product_count = 0

    if current_product_reviews:
        for review in current_product_reviews:
            product_sum += review.review_add_rating
            product_count += 1

        if product_sum > 0:
            instance.product.average_rating = round(
                                              product_sum/product_count) or 0
        else:
            instance.product.average_rating == 0
    else:
        instance.product.average_rating = 0

    instance.product.save()
