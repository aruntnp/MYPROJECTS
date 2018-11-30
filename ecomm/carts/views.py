from django.shortcuts import render, redirect
from .models import Cart
from accounts.forms import GuestForm
from addresses.forms import AddressForm
from addresses.models import Address

from products.models import Product
from orders.models import Order
from billing.models import BillingProfile


# Create your views here.

# def cart_create(user=None): # COMMENTED COZ" THIS IS ADDED IN MODEL MANAGER
#     cart_obj = Cart.objects.create(user = None)
#     print('xxxxxxxxxxxxxxxxxxx CART CREATED xxxxxxxxxxxxxxxx')
#     return cart_obj


def cart_home(request):
    # del request.session['cart_id']
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    return render(request, 'carts/home.html', {'cart': cart_obj})


def add_remove_to_cart(request):
    prod_id = request.POST.get('prod_pk')
    if prod_id is not None:
        try:
            prod_obj = Product.objects.get(pk=prod_id)
        except Product.DoesNotExist:
            print("Ooops Product deleted!!")
            return redirect(prod_obj.get_absolute_url())
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if prod_obj in cart_obj.products.all():
            cart_obj.products.remove(prod_obj)
        else:
            cart_obj.products.add(prod_obj)
    print(prod_obj.get_absolute_url())
    request.session['cart_items'] = cart_obj.products.count()
    return redirect(prod_obj.get_absolute_url())


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect('cart:home')
    next_url = request.build_absolute_uri
    billing_profile = None
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_form = AddressForm()
    # CODE REF VIDEO 089
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)


    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    #  SOME CODEs ARE COPIED TO MODEL MANAGER(BILLING)

    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id = shipping_address_id)
            del request.session['shipping_address_id']
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id = billing_address_id)
            del request.session['billing_address_id']
        if billing_address_id or shipping_address_id:
            order_obj.save()

    if request.method == 'POST':

        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            del request.session['cart_id']
            request.session['cart_items'] = 0
            return redirect('/cart/success')

    context = {
        'object': order_obj,
        'billing_profile': billing_profile,
        'absolute_uri': next_url,
        'form': guest_form,
        'address_form': address_form,
        'billing_address_form': billing_address_form,
    }
    return render(request, 'carts/checkout.html', context)
