"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from addresses import views as address_view
from products.views import ProductListView
from products import urls
from django.views.generic import TemplateView

from carts import urls

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^checkout/address/create/', address_view.CheckoutAddressView.as_view(), name='checkout_address_create'),
    url(r'^cart/', include('carts.urls', namespace='cart'), ),
    url(r'^products/', include('products.urls', namespace='prod')),
    url(r'^signup/$', accounts_views.SignUp.as_view(), name='signup'),
    url(r'^signup/guest/$', accounts_views.GuestLoginView.as_view(), name='guest_login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', accounts_views.MyLoginView.as_view(), name='login'),
    url(r'^login1/$', TemplateView.as_view(template_name='accounts/login.html'), name='login1'),

]

# ------- END _---------------------

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
