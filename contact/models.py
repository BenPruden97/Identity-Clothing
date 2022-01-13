from django.db import models

# Create your models here.


class FAQ(models.Model):
    """
    Define FAQS for contact page
    """

    question = models.CharField(max_length=254)
    answer = models.TextField()

    def __str__(self):
        return self.question

    def get_friendly_name(self):
        return self.answer
