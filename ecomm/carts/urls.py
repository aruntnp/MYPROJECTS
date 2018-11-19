from django.conf.urls import url

from .views import (
    cart_home,
    add_remove_to_cart,
    checkout_home,

)

urlpatterns = [

    url(r'^$', cart_home, name='cart'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', add_remove_to_cart, name='update'),

]
