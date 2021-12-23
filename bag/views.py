from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """
    View to return the bag.html page
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add quantity of clothing item to shopping bag
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product_size = None
    if 'size' in request.POST:
        product_size = request.POST['size']
    bag = request.session.get('bag', {})

    if product_size:
        if item_id in list(bag.keys()):
            if product_size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][product_size] += quantity
                messages.success(request, f'Updated size {product_size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][product_size]}')

            else:
                bag[item_id]['items_by_size'][product_size] = quantity
                messages.success(request, f'Added size {product_size.upper()} {product.name} to your shopping bag successfully')

        else:
            bag[item_id] = {'items_by_size': {product_size: quantity}}
            messages.success(request, f'Added size {product_size.upper()} {product.name} to your shopping bag successfully')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your shopping bag successfully')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust quantity of clothing item in shopping bag
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    product_size = None
    if 'size' in request.POST:
        product_size = request.POST['size']
    bag = request.session.get('bag', {})

    if product_size:
        if quantity > 0:
            bag[item_id]['items_by_size'][product_size] = quantity
            messages.success(request, f'Updated size {product_size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][product_size]}')
        else:
            del bag[item_id]['items_by_size'][product_size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {product_size.upper()} {product.name} from your shopping bag successfully')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your shopping bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove clothing item from shopping bag
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        product_size = None
        if 'size' in request.POST:
            product_size = request.POST['size']
        bag = request.session.get('bag', {})

        if product_size:
            del bag[item_id]['items_by_size'][product_size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {product_size.upper()} {product.name} from your shopping bag successfully')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your shopping bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
