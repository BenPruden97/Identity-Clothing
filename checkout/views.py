from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There is nothing in your shopping bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KBiOEGQbvpK4zsWUeLMPQ02UXFMojEJJ7XcXvu44CAvc55nmvFh0uXOHOs7vxyHVoAJZYslHMQZk0p5JEM5oenN00PekWdMFw',
    }

    return render(request, template, context)
