from django.db import models
from django.urls import reverse

import os
import random
from ecomm.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save


# Create your models here.

# ******************** EXTRAS ****************************
def upload_img_path(instance, filename):
    print(instance)
    print(' ')
    print(filename)
    new_filename = random.randint(0, 94743824)
    name, ext = get_file_ext(filename)
    final_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "product/{new_filename}/{name}/{final_name}".format(new_filename=new_filename, final_name=final_name,
                                                               name=name)


def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True, active=True)

    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):  # == Product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Product.objects == self.get_queryset

        if qs.count() == 1:
            return qs.first()
        return None

    def get_by_slug(self, slug):
        qs = self.get_queryset().filter(slug=slug, active=True)  # Product.object == self.get_queryset

        return qs


# ------------------- END EXTRAS -------------------------

class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')

    def __str__(self):
        _name = [self.title]
        _parent = self.parent

        while _parent is not None:
            _name.append(_parent.title)
            _parent = _parent.parent

        return ' -> '.join(_name[::-1])


GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('m&f', "Male & Female"),
    ('baby', 'Baby'),

)

class ProductDetail(models.Model):
    product = models.ForeignKey('Product', related_name='product_details')
    product_for = models.CharField(max_length=120, null=True, blank=True, choices=GENDER_CHOICES)
    product_type = models.CharField(max_length=180, null=True, blank=True)
    material = models.CharField(max_length=180, null=True, blank=True)
    product_size_available = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.product)


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.0)
    image = models.ImageField(upload_to=upload_img_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Catalog
    # Brand
    #

    objects = ProductManager()

    def get_absolute_url(self):
        val = reverse("prod:ProductDetailSlugView", kwargs={'slug': self.slug})
        # print(val)
        return val

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver, sender=Category)
