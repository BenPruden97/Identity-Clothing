from django.shortcuts import render
from .models import FAQ

# Create your views here.


def view_contact(request):
    """
    View to return the contact.html page
    """

    faqs = FAQ.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'contact.html', context)
