from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from products.models import Product



# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Add the product amount """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] = quantity
    else:
        if quantity > 0:
            print(f"BAG: {bag}")
            print(f"QUANTITY: {quantity}")
            bag[item_id]['quantity'] = quantity
        else:
            del bag[item_id]['quantity']

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    print("remove_from_bag function is called")
    print(f"item_id is {item_id}")
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    bag.pop(item_id)
    messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return HttpResponse(status=200)
    return redirect(redirect_url)
