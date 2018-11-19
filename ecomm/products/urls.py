from django.conf.urls import url

from .views import (
    ProductListView,
    ProductDetailView,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    ProductDetailSlugView,

)

urlpatterns = [

    url(r'^$', ProductListView.as_view(), name='home'),
    url(r'^$', ProductListView.as_view(), name='ProductListView'),

    # url(r'/(?P<pk>\d+)/$', ProductDetailView.as_view(), name = 'ProductDetailView'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='ProductDetailSlugView'),

    # url(r'^featured/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),

]
