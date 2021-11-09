from django.shortcuts import render

# Create your views here.

def index(request):
    """
    View to return the index.html page
    """

    return render(request, 'index.html')
