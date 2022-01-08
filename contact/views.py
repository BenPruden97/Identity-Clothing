from django.shortcuts import render

# Create your views here.


def view_contact(request):
    """
    View to return the contact.html page
    """

    return render(request, 'contact.html')
