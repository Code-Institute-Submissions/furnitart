from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, PreOrder
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Profile could not be updated!')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    preorders = profile.preorders.all()
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
        'preorders': preorders,
        'form': form,
        'on_profile_page': True,
        
    }
    for order in orders:
        print(order.lineitems)
    return render(request, template, context)

def order_history(request, order_number):
    """view showing sepcific order """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can see that.')
        return redirect(reverse('home'))
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def pre_order_history(request, order_number):
    """view showing sepcific preorder """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can see that.')
        return redirect(reverse('home'))
    order = get_object_or_404(PreOrder, order_number=order_number)
    messages.info(request, (
        f'This is a past confirmation for pre order number {order_number}. '
        'Payment instructions  were sent on the order date.'
    ))

    template = 'checkout/invoice_confirmation.html'
    context = {
        'order': order,
        'from_profile': True,
        }

    return render(request, template, context)
    