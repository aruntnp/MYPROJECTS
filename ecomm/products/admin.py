from django.contrib import admin
from .models import Product, Category, ProductDetail, ProductImage
# Register your models here.

class ImagesInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'pk']
    inlines = [
        ImagesInline,
    ]
    class Meta:
        model = Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug','pk']

    class Meta:
        model= Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductDetail)