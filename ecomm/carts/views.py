from django.shortcuts import render, redirect
from .models import Cart
from accounts.forms import GuestForm
from accounts.models import GuestEmail
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
    else:
        # print('Login Mode -------------')
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
        billing_profile = None
        guest_form = GuestForm()
        guest_email_id = request.session.get('guest_email_id')
        user = request.user
        next_url = request.build_absolute_uri
        if user.is_authenticated():
            billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user, email=user.email)
        elif guest_email_id is not None:
            guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
            billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(email=guest_email_obj.email)
        else:
            pass
            #RAISE ERROR

    context = {
        'object': order_obj,
        'billing_profile': billing_profile,
        'absolute_uri': next_url,
        'form': guest_form
    }
    return render(request, 'carts/checkout.html', context)
