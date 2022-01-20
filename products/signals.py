from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.db.models import Sum

from .models import ProductReview

@receiver(post_save, sender=ProductReview)
def ben_find_averages(sender, instance, created, **kwargs):
    """
    Update product average_rating on rating_add_rating update/create
    """
    current_product = instance.product
    print("average rating", (current_product))

    current_product_reviews = ProductReview.objects.filter(product=current_product)

    print("average rating", (current_product_reviews))

    product_sum = 0
    product_count = 0

    for review in current_product_reviews:
        product_sum += review.review_add_rating
        product_count += 1

    print("sum", product_sum)
    print("product_count", product_count)

    print("average rating", round(product_sum/product_count))

    instance.product.average_rating = round(product_sum/product_count)

    print("rating", instance.product.average_rating)

    instance.product.save()

@receiver(post_delete, sender=ProductReview)
def ben_averages(sender, instance, **kwargs):
    """
    Update product average_rating on rating_add_rating delete
    """
    instance.product_id.average_rating()
