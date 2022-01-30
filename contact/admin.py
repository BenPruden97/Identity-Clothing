"""
Contact admin view to create the admin view for FAQs
"""

from django.contrib import admin
from .models import FAQ

# Register your models here.


class FAQAdmin(admin.ModelAdmin):
    """
    Admin views for FAQs
    """
    list_display = (
        'question',
        'answer',
    )


admin.site.register(FAQ, FAQAdmin)
