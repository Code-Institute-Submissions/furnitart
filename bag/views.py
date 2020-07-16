from django.shortcuts import render, redirect,reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def bag (request):
    """returns bag page"""
    
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """ Remove a specific product from the shopping bag """

    bag = request.session.get('bag', {})
    try:
        del bag[item_id]
        request.session['bag'] = bag
    except KeyError as ex:
        print("No such key: '%s'" % ex.message)
    return redirect("view_bag")

def update_bag(request, item_id):
    """ amend the amount of a specific item in the bag"""
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    bag[item_id] = quantity
    request.session['bag'] = bag
    return redirect("view_bag")

def remove_from_bag(request, item_id):
    """ Remove a specific product from the shopping bag """

    bag = request.session.get('bag', {})
    try:
        del bag[item_id]
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)