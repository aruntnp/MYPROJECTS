from django.contrib import admin
from .models import Product, Category, ProductDetail
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug','pk']

    class Meta:
        model= Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug','pk']

    class Meta:
        model= Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductDetail)