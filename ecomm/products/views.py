from django.views.generic import ListView, DetailView
# from django.shortcuts import render
from django.http import Http404
from .models import Product, ProductImage

from carts.models import Cart
# from django.urls import reverse

# Create your views here.
# ---------- CLASS BASED DETAIL VIEW INSTANCES(OBJECTS)----------------
# { 'paginator': None,
#   'page_obj': None,
#   'is_paginated': False,
#   'object_list': <QuerySet [<Product: Basic Shirt>]>,
#   'product_list': <QuerySet [<Product: Basic Shirt>]>,
#   'view': <products.views.ProductListView object at 0x0000020698D5FDA0>}

# --------- CLASS BASED LIST VIEW INSTANCES(OBJECTS)-------------------
# {'paginator': None,
# 'page_obj': None,
# 'is_paginated': False,

# 'object_list': <QuerySet [<Product: Basic Shirt>, <Product: Allen Solly>]>,

# 'product_list': <QuerySet [<Product: Basic Shirt>, <Product: Allen Solly>]>,

# 'view': <products.views.ProductListView object at 0x000001BCD5B3D898>}

# ***************************************** PRODUCT SLUG VIEW **************************************

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        # context['product'] = Product.objects.all()
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:

            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404('Ooops Product Does not exist... :-(')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404('Something went wrong.. ')
        print("inst -- "+str(instance))

        # val = ProductImage.objects.get(product = instance).first()
        # instance = val
        print(instance)
        return instance



# ****************************************** PRODUCT VIEWS ******************************************

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        # print(context)
        return context


    def get_queryset(self, *args, **kwargs):
        request = self.request
        # pk = self.kwargs.get('pk')
        return Product.objects.all()






class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)

        if instance is None:
            raise Http404('Product not avaiable by Aroon..')
        return instance




    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


# ****************************************** FEATURED VIEWS ******************************************

class ProductFeaturedListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs): # get_queryset == Product.objects
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/featured-detail.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()